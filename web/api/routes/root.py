from api.values import HTTPResponseCode
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse


def routes_root_view(request: WSGIRequest) -> HttpResponse:
    """
    Process the api root page.

    Args:
        request: WSGIRequest

    Returns:
        HttpResponse
    """
    return HttpResponse(
        '404 Not Found',
        status=HTTPResponseCode.not_found,
    )
