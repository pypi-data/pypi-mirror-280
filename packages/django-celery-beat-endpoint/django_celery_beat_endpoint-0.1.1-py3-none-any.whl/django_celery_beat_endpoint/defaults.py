DEFAULT_PORT = 8005
DEFAULT_HTTP_SERVER = "django_celery_beat_endpoint.backends:HTTPServer"

DEFAULTS = {
    "beat_port": DEFAULT_PORT,
    "beat_http_server": DEFAULT_HTTP_SERVER,
}
