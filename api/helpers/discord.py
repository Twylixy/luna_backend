from typing import Optional

from api.database.models import TokenModel
from api.entities.discord import OAuth2TokenCredentials
from api.services.discord import get_discord_user, refresh_oauth2_credentials


def revoke_token_credentials(
    old_token: TokenModel,
) -> Optional[OAuth2TokenCredentials]:
    """
    Revoke token credentials until it valid.

    Args:
      old_token: OAuth2TokenCredentials
    Returns:
      Optional[OAuth2TokenCredentials]
    """
    token_object = refresh_oauth2_credentials(old_token.refresh_token)

    if token_object is None:
        return None

    user = get_discord_user(token_object.access_token)

    if user is None:
        return None

    return token_object
