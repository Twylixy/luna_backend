# HTTP response codes
# refer to https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
class HTTPResponseCode:
    """Represents HTTP response codes."""

    ok = 200
    bad_request = 400
    unauthorized = 401
    forbidden = 403
    not_found = 404
    method_not_allowed = 405
    internal_server_error = 500
