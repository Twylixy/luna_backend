from rest_framework.authentication import TokenAuthentication


class BearerAuthentication(TokenAuthentication):
    """Represents Bearer token authentication."""

    keyword = 'Bearer'
