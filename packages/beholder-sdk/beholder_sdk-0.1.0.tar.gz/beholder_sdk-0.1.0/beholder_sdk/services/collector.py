import traceback
import uuid
import inspect
import os
import sys
import time
from time import strftime, localtime
import linecache
import requests
import datetime
from sqlalchemy import event
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlparse
from sqlparse.sql import IdentifierList, Identifier
from sqlparse.tokens import Keyword, DML
from abc import ABC, abstractmethod
from beholder_sdk.database.models import RequestTrace, Service, RequestResponse, CodeLine, DBRequestResponse, \
    StackTrace, SaveAllFlag
from beholder_sdk.database.db_connector import coonect_to_db


class Collector(ABC):
    def __init__(self, db_engine):
        self.temp_storage = {'trace': [],
                             'db_request': [],
                             'response': {"status_line": 500, "headers": None, "body": None},
                             'error': '', 'error_message': '', 'error_type': '', 'last_event': ''}
        self.app_directory = self._determine_app_directory()
        try:
            self.engine = db_engine
            db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=self.engine))
            Base = declarative_base()
            Base.query = db_session.query_property()
            self._setup_db_event_listeners()
            self.save_to_db = 1
        except:
            self.save_to_db = 0
        try:
            self.db_session = coonect_to_db()
            self.save_flag = self._get_save_flag()
        except:
            self.save_flag = 0

    def _clean_temp_storage(self):
        try:
            self.save_flag = self._get_save_flag()
        except:
            self.save_flag = 0
        self.temp_storage = {'trace': [],
                             'db_request': [],
                             'response': {"status_line": 500, "headers": None, "body": None},
                             'error': '', 'error_message': '', 'error_type': '', 'last_event': ''}

    def _get_save_flag(self):
        flag_obj = self.db_session.query(SaveAllFlag).filter(SaveAllFlag.id == 1).first()
        return flag_obj.flag

    def _determine_app_directory(self):
        frame = inspect.stack()[-1]
        module = inspect.getmodule(frame[0])
        return os.path.dirname(os.path.abspath(module.__file__))

    def _before_request(self, request):
        self.store_correlation(request)
        self.store_request(request)
        sys.settrace(self.localtrace)

    def _after_request(self, response):
        self.store_response(response)
        return response

    def _handle_exception(self, exception):
        if self.get_created_correlation():
            self.save_flag = 1
        if exception:
            self.save_flag = 1
            self.store_exception(exception)
        self.log_data()
        self._clean_temp_storage()
        sys.settrace(None)

    def store_correlation(self, request):
        correlation_id = request.headers.get('X-Correlation-ID', str(uuid.uuid4()))
        request_from = request.headers.get('Service-ID', None)
        request_to = str(uuid.uuid4())
        self.temp_storage["correlation_id"] = correlation_id
        self.temp_storage["request_from"] = request_from
        self.temp_storage["request_to"] = request_to

    def store_request(self, request):
        self.temp_storage["request"] = self.extract_request_info(request)
        self.temp_storage["request"]["request_time"] = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        self.temp_storage["address"] = str(self.temp_storage["request"]["headers"]["Host"])

    def store_response(self, response):
        self.temp_storage["response"] = self.extract_response_info(response)
        self.temp_storage["response"]["response_time"] = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

    def store_exception(self, exception):
        exception_type = exception.__class__.__name__
        self.temp_storage["error"] = ''.join(traceback.format_tb(exception.__traceback__))
        self.temp_storage["error_type"] = exception_type
        self.temp_storage["error_message"] = str(exception)
        self.temp_storage["response"]["response_time"] = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

    def store_database_request(self, db_request):
        self.temp_storage["db_request"] = db_request

    def store_database_response(self, db_response):
        self.temp_storage["db_response"] = db_response

    def get_created_correlation(self):
        correlation = self.db_session.query(RequestTrace).filter(
            RequestTrace.id == self.temp_storage['correlation_id']).one_or_none()
        return correlation

    def create_correlation(self):
        correlation_object = RequestTrace(id=self.temp_storage['correlation_id'])
        self.create_object(correlation_object)

    def create_object(self, obj):
        self.db_session.add(obj)
        self.db_session.commit()
        self.db_session.refresh(obj)

    def _setup_db_event_listeners(self):
        @event.listens_for(self.engine, "before_cursor_execute")
        def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
            parsed = sqlparse.parse(statement)
            query_type = self._get_query_type(parsed)
            target_tables = self._get_target_table(parsed, query_type)
            self.temp_storage['db_request'].append({
                'database_url': str(self.engine.url),
                'db_user': self.engine.url.username,
                'db_schema': self.engine.url.database,
                'statement': statement,
                'parameters': parameters,
                'affected_rows': None,
                'filename': self.temp_storage['trace'][-1][1],
                'lineno': self.temp_storage['trace'][-1][2],
                'query_type': query_type,
                'target_tables': target_tables,
                'status': 'running',
                'start_time': time.time(),
                'end_time': None,
                'duration': None,
            })

        @event.listens_for(self.engine, "after_cursor_execute")
        def after_cursor_execute(conn, cursor, statement, parameters, context, executemany):
            start_time = strftime('%Y-%m-%d %H:%M:%S', localtime(self.temp_storage['db_request'][-1]['start_time']))
            end_time = time.time()
            duration = end_time - self.temp_storage['db_request'][-1]['start_time']
            end_time = strftime('%Y-%m-%d %H:%M:%S', localtime(end_time))
            rows_returned = cursor.rowcount
            self.temp_storage['db_request'][-1].update({
                'start_time': start_time,
                'status': 'Success',
                'affected_rows': rows_returned,
                'end_time': end_time,
                'duration': duration
            })

        @event.listens_for(self.engine, "handle_error")
        def handle_error(context):
            start_time = strftime('%Y-%m-%d %H:%M:%S', localtime(self.temp_storage['db_request'][-1]['start_time']))
            end_time = time.time()
            duration = end_time - self.temp_storage['db_request'][-1]['start_time']
            end_time = strftime('%Y-%m-%d %H:%M:%S', localtime(end_time))
            self.temp_storage['db_request'][-1].update({
                'start_time': start_time,
                'status': 'Error',
                'affected_rows': str(context),
                'end_time': end_time,
                'duration': duration
            })

    def localtrace(self, frame, event, arg):
        if event in ('line', 'call', 'return', 'exception'):
            self.store_trace(frame, event, arg)
        return self.localtrace

    def store_trace(self, frame, event, arg):
        filename = frame.f_code.co_filename
        if self._is_user_code(filename):
            if self.temp_storage['last_event'] == 'call':
                lineno = frame.f_lineno - 1
                variables = {}
                code_line = linecache.getline(filename, lineno)
                self.temp_storage['trace'].append(('call', filename, lineno, code_line, variables))
            if event == 'line':
                lineno = frame.f_lineno
                variables = self.collect_variables(frame)
                variables = self.convert_to_serializable(variables)
                code_line = linecache.getline(filename, lineno)
                self.temp_storage['trace'].append((event, filename, lineno, code_line, variables))
        self.temp_storage['last_event'] = event

    def _is_user_code(self, filename):
        return filename.startswith(self.app_directory) and not any(
            filename.startswith(path) for path in sys.path if 'site-packages' in path or 'dist-packages' in path) and (
                ".py" in filename)

    def collect_variables(self, frame):
        return {key: value for key, value in frame.f_locals.items()}

    def log_data(self):
        if self.save_flag:
            if not self.get_created_correlation():
                self.create_correlation()
            if self.save_to_db:
                self.save_data_to_db()
            else:
                self.save_data_to_file()

    def save_data_to_db(self):
        service = Service(id=self.temp_storage['request_to'],
                          name=self.app.name,
                          address=self.temp_storage["address"],

                          request_trace_id=self.temp_storage['correlation_id'])
        self.create_object(service)

        request_response = RequestResponse(id=str(uuid.uuid4()),
                                           request_url=self.temp_storage["request"]["request_url"],
                                           request_method=self.temp_storage["request"]["request_method"],
                                           request_headers=self.temp_storage["request"]["headers"],
                                           request_body=self.temp_storage["request"]["body"],
                                           request_params=self.temp_storage["request"]["params"],
                                           request_time=self.temp_storage["request"]["request_time"],

                                           response_status=self.temp_storage["response"]["status_line"],
                                           response_headers=self.temp_storage["response"]["headers"],
                                           response_body=self.temp_storage["response"]["body"],
                                           response_time=self.temp_storage["response"]["response_time"],

                                           request_from=self.temp_storage["request_from"],
                                           request_to_id=self.temp_storage["request_to"],

                                           request_trace_id=self.temp_storage['correlation_id'])
        self.create_object(request_response)

        stacktrace = StackTrace(id=str(uuid.uuid4()),
                                stack_trace=self.temp_storage["error"],
                                error_message=self.temp_storage["error_message"],
                                error_type=self.temp_storage["error_type"],

                                service_id=self.temp_storage["request_to"],

                                request_trace_id=self.temp_storage['correlation_id'])
        self.create_object(stacktrace)

        for i in range(len(self.temp_storage["db_request"])):
            db_request_response = DBRequestResponse(id=str(uuid.uuid4()),
                                                    query=self.temp_storage['db_request'][i]['statement'],
                                                    query_parameters=self.temp_storage['db_request'][i]['parameters'],
                                                    affected_rows=self.temp_storage['db_request'][i]['affected_rows'],
                                                    filename=self.temp_storage['db_request'][i]['filename'],
                                                    lineno=self.temp_storage['db_request'][i]['lineno'],

                                                    request_from_id=self.temp_storage["request_to"],
                                                    request_to=self.temp_storage['db_request'][i]['database_url'],
                                                    db_user=self.temp_storage['db_request'][i]['db_user'],
                                                    db_schema=self.temp_storage['db_request'][i]['db_schema'],

                                                    query_type=self.temp_storage['db_request'][i]['query_type'],
                                                    target_tables=self.temp_storage['db_request'][i]['target_tables'],
                                                    status=self.temp_storage['db_request'][i]['status'],

                                                    start_time=self.temp_storage['db_request'][i]['start_time'],
                                                    end_time=self.temp_storage['db_request'][i]['end_time'],
                                                    duration=self.temp_storage['db_request'][i]['duration'],

                                                    request_trace_id=self.temp_storage['correlation_id'])
            self.create_object(db_request_response)

        for line in self.temp_storage['trace']:
            codeline = CodeLine(id=str(uuid.uuid4()),
                                event=line[0],
                                filename=line[1],
                                lineno=line[2],
                                code_line=line[3],
                                variables=line[4],

                                service_id=self.temp_storage["request_to"],

                                request_trace_id=self.temp_storage['correlation_id'])
            self.create_object(codeline)

    def save_data_to_file(self):
        with open("log.txt", "w") as log:
            service = str({
                "id": self.temp_storage['request_to'],
                "name": self.app.name,
                "address": self.temp_storage["address"],

                "request_trace": self.temp_storage['correlation_id']
            })
            log.write(str(service))
            request_response = str({
                "id": str(uuid.uuid4()),
                "request_url": self.temp_storage["request"]["request_url"],
                "request_method": self.temp_storage["request"]["request_method"],
                "request_headers": self.temp_storage["request"]["headers"],
                "request_body": self.temp_storage["request"]["body"],
                "request_params": self.temp_storage["request"]["params"],
                "request_time": self.temp_storage["request"]["request_time"],

                "response_status": self.temp_storage["response"]["status_line"],
                "response_headers": self.temp_storage["response"]["headers"],
                "response_body": self.temp_storage["response"]["body"],
                "response_time": self.temp_storage["response"]["response_time"],

                "request_from": self.temp_storage["request_from"],
                "request_to": self.temp_storage["request_to"],

                "request_trace": self.temp_storage['correlation_id']
            })
            log.write(str(request_response))
            stacktrace = str({
                "id": str(uuid.uuid4()),
                "stack_trace": self.temp_storage["error"],
                "error_message": self.temp_storage["error_message"],

                "service": self.temp_storage["request_to"],

                "request_trace": self.temp_storage['correlation_id']
            })
            log.write(str(stacktrace))
            db_request = []
            for i in range(len(self.temp_storage["db_request"])):
                db_request.append({
                    "id": str(uuid.uuid4()),
                    "query": self.temp_storage['db_request'][i]['statement'],
                    "query_parameters": self.temp_storage['db_request'][i]['parameters'],
                    "affected_rows": "",
                    "filename": self.temp_storage['db_request'][i]['filename'],
                    "lineno": self.temp_storage['db_request'][i]['lineno'],

                    "request_from": self.temp_storage["request_to"],
                    "request_to": self.temp_storage['db_request'][i]['database_url'],

                    "request_trace": self.temp_storage['correlation_id']
                })
            log.write(str(db_request))
            codelines = []
            for line in self.temp_storage['trace']:
                codelines.append({
                    "id": str(uuid.uuid4()),
                    "event": line[0],
                    "filename": line[1],
                    "lineno": line[2],
                    "code_line": line[3],
                    "variables": line[4],

                    "service": self.temp_storage["request_to"],

                    "request_trace": self.temp_storage['correlation_id']
                })
            log.write(str(codelines))

    def send_request(self, url, method='GET', data=None):
        headers = {
            'X-Correlation-ID': self.temp_storage['correlation_id'],
            'Service-ID': self.temp_storage['request_to']
        }
        response = requests.request(method, url, headers=headers, json=data)
        return response

    def _get_query_type(self, parsed):
        for stmt in parsed:
            for token in stmt.tokens:
                if token.ttype is DML:
                    return token.value
        return None

    def _get_target_table(self, parsed, query_type):
        if not query_type:
            return None

        keywords_to_look_for = {
            'SELECT': 'FROM',
            'INSERT': 'INTO',
            'UPDATE': 'UPDATE',
            'DELETE': 'FROM'
        }

        keyword = keywords_to_look_for.get(query_type)
        if not keyword:
            return None

        for stmt in parsed:
            from_seen = False
            for token in stmt.tokens:
                if from_seen:
                    if isinstance(token, Identifier):
                        return token.get_real_name()
                    elif isinstance(token, IdentifierList):
                        for identifier in token.get_identifiers():
                            if identifier.get_real_name():
                                return identifier.get_real_name()
                if token.ttype is Keyword and token.value.upper() == keyword:
                    from_seen = True
        return None

    def convert_to_serializable(self, obj):
        if isinstance(obj, dict):
            return {k: self.convert_one_element(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self.convert_one_element(v) for v in obj]
        elif hasattr(obj, '__dict__'):
            return {k: self.convert_one_element(v) for k, v in obj.__dict__.items()}
        else:
            return str(repr(obj))

    def convert_one_element(self, obj):
        return str(repr(obj))


    @abstractmethod
    def extract_request_info(self, request):
        raise NotImplementedError("Must be implemented by subclasses.")

    @abstractmethod
    def extract_response_info(self, response):
        raise NotImplementedError("Must be implemented by subclasses.")
