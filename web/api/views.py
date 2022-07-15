from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse


def root_api_view(request: WSGIRequest) -> HttpResponse:
    """
    Process the api root page.

    Args:
        request: WSGIRequest

    Returns:
        HttpResponse
    """
    return HttpResponse('Forbidden (403)', status=403)
