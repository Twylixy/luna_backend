from api.values import HTTPResponseCode
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def test_healthcheck_view(request: WSGIRequest) -> HttpResponse:
    """
    Test whether the backend is ready.

    Args:
        request: WSGIRequest
    Returns:
        HttpResponse
    """
    return HttpResponse('200 OK', status=HTTPResponseCode.ok)
