# error_collector/middleware_flask.py
from flask import request
from beholder_sdk.services.collector import Collector


class FlaskCollectorMiddleware(Collector):
    def __init__(self, app, db_url):
        super().__init__(db_url)
        self.app = app
        self.app.before_request(self.before_request)
        self.app.after_request(self.after_request)
        self.app.teardown_request(self.handle_exception)

    def before_request(self):
        super()._before_request(request)

    def after_request(self, response):
        return super()._after_request(response)

    def handle_exception(self, exception):
        super()._handle_exception(exception)

    def extract_request_info(self, request):
        return {
            'request_method': request.method,
            'request_url': request.url,
            'headers': dict(request.headers),
            'body': request.get_data().decode('utf8'),
            'params': request.args
        }

    def extract_response_info(self, response):
        return {
            'status_line': response.status,
            'headers': dict(response.headers),
            'body': response.get_data().decode('utf8')
        }

