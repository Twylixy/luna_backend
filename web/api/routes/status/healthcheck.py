from api.values import HTTPResponseCode
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse


def test_healthcheck_view(request: WSGIRequest) -> HttpResponse:
    """
    Test whether the backend is ready.

    Args:
        request: WSGIRequest
    Returns:
        HttpResponse
    """
    return HttpResponse('200 OK', status=HTTPResponseCode.ok)
