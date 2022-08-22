import json
import os
import secrets
from datetime import datetime, timedelta

from api.helpers.discord import get_discord_user, get_oauth2_credentials
from api.models import TokensModel, UserModel
from api.requests.auth.discord_request import DiscordAuthRequest
from api.responses.auth.discord_response import DiscordAuthResponse
from api.responses.error_response import ErrorResponse
from api.values import HTTPResponseCode
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import JsonResponse
from drf_spectacular.utils import extend_schema
from pydantic import ValidationError
from rest_framework.decorators import api_view


@extend_schema(
    request={'application/json': DiscordAuthRequest.schema()},
    responses={
        HTTPResponseCode.ok: DiscordAuthResponse.schema(),
        HTTPResponseCode.bad_request: ErrorResponse.schema(),
    },
)
@api_view(['POST'])
def auth_discord_view(request: WSGIRequest) -> JsonResponse:
    """
    Process the /api/auth/discord.

    Args:
        request: WSGIRequest

    Returns:
        JsonResponse
    """
    try:
        discord_auth_request = DiscordAuthRequest.parse_obj(json.loads(request.body))
    except ValidationError:
        response = {
            'status': 'failure',
            'message': 'wrong request body',
        }

        return JsonResponse(
            ErrorResponse.parse_obj(response).dict(),
            status=HTTPResponseCode.bad_request,
        )

    if discord_auth_request.code == 'test':
        response = {
            'status': 'success',
            'token': 'there will be a token',
        }

        return JsonResponse(
            DiscordAuthResponse.parse_obj(response).dict(),
            status=HTTPResponseCode.ok,
        )

    oauth2_credentials = get_oauth2_credentials(
        discord_auth_request.code,
        discord_auth_request.redirect_uri,
    )

    if oauth2_credentials is None:
        response = {
            'status': 'failure',
            'message': 'unable to get oauth2 credentials',
        }

        return JsonResponse(
            ErrorResponse.parse_obj(response).dict(),
            status=HTTPResponseCode.bad_request,
        )

    discord_user = get_discord_user(oauth2_credentials.access_token)

    if discord_user is None:
        response = {
            'status': 'failure',
            'message': 'unable to get user from discord',
        }

        return JsonResponse(
            ErrorResponse.parse_obj(response).dict(),
            status=HTTPResponseCode.bad_request,
        )

    user_object, _ = UserModel.objects.get_or_create(
        discord_id=discord_user.id,
    )
    token_object, _ = TokensModel.objects.get_or_create(
        discord_id=user_object,
    )

    token_object.token = secrets.token_hex(
        int(os.getenv('TOKEN_LENGTH', '32')),
    )
    token_object.discord_token = oauth2_credentials.access_token
    token_object.discord_refresh_token = oauth2_credentials.refresh_token
    token_object.epires = datetime.now() + timedelta(
        seconds=oauth2_credentials.expires_in,
    )

    user_object.email = discord_user.email

    token_object.save()
    user_object.save()

    response = {
        'status': 'success',
        'token': token_object.token,
    }

    return JsonResponse(
        DiscordAuthResponse.parse_obj(response).dict(),
        status=HTTPResponseCode.ok,
    )
