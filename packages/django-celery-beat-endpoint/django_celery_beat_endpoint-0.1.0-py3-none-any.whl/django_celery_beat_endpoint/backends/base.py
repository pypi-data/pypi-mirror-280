import http.server
import json
import traceback
from http import HTTPStatus

from django_celery_beat_endpoint.beat import AwareBeat


def exception_handler(func):
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as exc:
            self.send_error(
                code=HTTPStatus.INTERNAL_SERVER_ERROR,
                explain=str(exc),
            )
            self.log_error(traceback.format_exc())

    return wrapper


class JsonHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def __init__(self, *args, beat: "AwareBeat", **kwargs) -> None:
        self.beat = beat
        super().__init__(*args, **kwargs)

    def send_json(self, data, code=None):
        if code is None:
            code = HTTPStatus.OK
        self.send_response(code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def _handle_status(self):
        try:
            self.beat.ping()
            self.send_json({"status": HTTPStatus.OK.name})
        except Exception as exc:
            self.send_json({"status": str(exc)}, code=HTTPStatus.INTERNAL_SERVER_ERROR)

    @exception_handler
    def _handle_tasks(self):
        response = self.beat.get_periodic_tasks()
        self.send_json(response)

    def do_GET(self):
        if self.path == "/status":
            self._handle_status()
        elif self.path == "/tasks":
            self._handle_tasks()
        else:
            self.send_error(HTTPStatus.NOT_FOUND)


class BaseHTTPServer:
    def __init__(self, beat, port) -> None:
        self.beat = beat
        self.port = port

    def serve(self):
        raise NotImplementedError


class HTTPServer(BaseHTTPServer):
    def serve(self):
        handler = lambda *args, **kwargs: JsonHTTPRequestHandler(
            *args, beat=self.beat, **kwargs
        )
        with http.server.HTTPServer(("", self.port), handler) as httpd:
            httpd.serve_forever()
