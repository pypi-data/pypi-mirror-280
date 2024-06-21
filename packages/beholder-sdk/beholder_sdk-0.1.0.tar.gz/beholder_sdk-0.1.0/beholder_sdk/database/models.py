from sqlalchemy import Column, String, Integer, Text, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, declarative_base
import uuid

Base = declarative_base()


class RequestTrace(Base):
    __tablename__ = 'beholder_requesttrace'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)


class SaveAllFlag(Base):
    __tablename__ = 'beholder_saveallflag'
    id = Column(Integer, primary_key=True, default=1, nullable=False)
    flag = Column(Integer, nullable=False)


class Service(Base):
    __tablename__ = 'beholder_service'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    name = Column(String, nullable=False)
    address = Column(Text, nullable=False)

    request_trace_id = Column(UUID(as_uuid=True), nullable=False)
    # request_trace = relationship('RequestTrace', back_populates='services')


# RequestTrace.services = relationship('Service', order_by=Service.id, back_populates='request_trace')


class RequestResponse(Base):
    __tablename__ = 'beholder_requestresponse'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    request_url = Column(String, nullable=False)
    request_method = Column(String(10), nullable=False)
    request_headers = Column(JSON, nullable=False)
    request_body = Column(JSON, nullable=False)
    request_params = Column(JSON, nullable=False)
    request_time = Column(String, nullable=False)

    response_status = Column(String, nullable=False)
    response_headers = Column(JSON, nullable=False)
    response_body = Column(JSON, nullable=False)
    response_time = Column(String, nullable=False)

    request_from = Column(UUID(as_uuid=True), nullable=True)
    request_to_id = Column(UUID(as_uuid=True), nullable=False)
    request_trace_id = Column(UUID(as_uuid=True), nullable=False)

    # request_from = relationship('Service', foreign_keys=[request_from_id], back_populates='requests_from')
    # request_to = relationship('Service', foreign_keys=[request_to_id], back_populates='requests_to')
    # request_trace = relationship('RequestTrace', back_populates='requests')


# Service.requests_from = relationship('RequestResponse', foreign_keys=[RequestResponse.request_from_id],
#                                      back_populates='request_from')
# Service.requests_to = relationship('RequestResponse', foreign_keys=[RequestResponse.request_to_id],
#                                    back_populates='request_to')
# RequestTrace.requests = relationship('RequestResponse', order_by=RequestResponse.id, back_populates='request_trace')


class CodeLine(Base):
    __tablename__ = 'beholder_codeline'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    event = Column(String, nullable=False)
    filename = Column(Text, nullable=False)
    lineno = Column(Integer, nullable=False)
    code_line = Column(Text, nullable=False)
    variables = Column(JSON, nullable=False)

    service_id = Column(UUID(as_uuid=True), nullable=False)
    request_trace_id = Column(UUID(as_uuid=True), nullable=False)

    # service = relationship('Service', back_populates='codelines')
    # request_trace = relationship('RequestTrace', back_populates='codelines')


# Service.codelines = relationship('CodeLine', order_by=CodeLine.id, back_populates='service')
# RequestTrace.codelines = relationship('CodeLine', order_by=CodeLine.id, back_populates='request_trace')


class DBRequestResponse(Base):
    __tablename__ = 'beholder_dbrequestresponse'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    query = Column(Text, nullable=False)
    query_parameters = Column(JSON, nullable=False)
    affected_rows = Column(String, nullable=False)
    filename = Column(Text, nullable=False)
    lineno = Column(Integer, nullable=False)

    request_from_id = Column(UUID(as_uuid=True), nullable=False)
    request_to = Column(Text, nullable=False)
    db_user = Column(Text, nullable=True)
    db_schema = Column(Text, nullable=True)

    query_type = Column(Text, nullable=True)
    target_tables = Column(JSON, nullable=True)
    status = Column(Text, nullable=True)

    start_time = Column(Text, nullable=True)
    end_time = Column(Text, nullable=True)
    duration = Column(Text, nullable=True)

    request_trace_id = Column(UUID(as_uuid=True), nullable=False)

    # request_from = relationship('Service', back_populates='db_requests')
    # request_trace = relationship('RequestTrace', back_populates='db_requests')


# Service.db_requests = relationship('DBRequestResponse', order_by=DBRequestResponse.id, back_populates='request_from')
# RequestTrace.db_requests = relationship('DBRequestResponse', order_by=DBRequestResponse.id,
#                                         back_populates='request_trace')


class StackTrace(Base):
    __tablename__ = 'beholder_stacktrace'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    stack_trace = Column(Text, nullable=False)
    error_message = Column(Text, nullable=False)
    error_type = Column(Text, nullable=True)

    service_id = Column(UUID(as_uuid=True), nullable=False)
    request_trace_id = Column(UUID(as_uuid=True), nullable=False)

    # service = relationship('Service', back_populates='stacktraces')
    # request_trace = relationship('RequestTrace', back_populates='stacktraces')


# Service.stacktraces = relationship('StackTrace', order_by=StackTrace.id, back_populates='service')
# RequestTrace.stacktraces = relationship('StackTrace', order_by=StackTrace.id, back_populates='request_trace')
