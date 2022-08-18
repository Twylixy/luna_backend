from typing import Optional


def get_authorization_token(authorization_header_value: str) -> Optional[str]:
    """
    Extract token from authorization header.

    Args:
        authorization_header_value: str
    Returns:
        Optional[str]
    """
    authorization = authorization_header_value.split()

    if len(authorization) != 2 or authorization[0] != 'Bearer':
        return None

    return authorization[1]
