# error_collector/middleware_django.py
from django.utils.deprecation import MiddlewareMixin
from beholder_sdk.services.collector import Collector


class DjangoCollectorMiddleware(MiddlewareMixin, Collector):
    def __init__(self, app, db_url):
        super().__init__(db_url)

    def process_request(self, request):
        super()._before_request(request)

    def process_response(self, request, response):
        super()._after_request(response)

    def process_exception(self, request, exception):
        super()._handle_exception(exception)

    def extract_request_info(self, request):
        return {
            'start_line': f"{request.method} {request.get_full_path()}",
            'headers': dict(request.headers),
            'body': request.body,
            'params': request.GET
        }

    def extract_response_info(self, response):
        return {
            'status_line': response.status_code,
            'headers': dict(response.items()),
            'body': response.content
        }
