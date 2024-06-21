# error_collector/middleware_fastapi.py
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from beholder_sdk.services.collector import Collector


class FastApiCollectorMiddleware(BaseHTTPMiddleware, Collector):
    def __init__(self, app, db_url):
        super().__init__(db_url)
        self.app = app

    async def dispatch(self, request: Request, call_next):
        self._before_request(request)
        try:
            response = await call_next(request)
        except Exception as e:
            super()._handle_exception(e)
            raise e

        return self._after_request(response)

    async def extract_request_info(self, request):
        return {
            'start_line': f"{request.method} {request.url}",
            'headers': dict(request.headers),
            'body': await request.body(),
            'params': dict(request.query_params)
        }

    async def extract_response_info(self, response):
        return {
            'status_line': response.status_code,
            'headers': dict(response.headers),
            'body': b''.join([chunk async for chunk in response.body_iterator])
        }
