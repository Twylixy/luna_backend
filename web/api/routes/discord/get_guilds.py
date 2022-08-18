from datetime import datetime, timedelta

from api.authentication import BearerAuthentication
from api.helpers.authorization import get_authorization_token
from api.helpers.discord import get_user_guilds, refresh_oauth2_credentials
from api.models import TokensModel, UserModel
from api.requests.discord.get_guilds_request import GetGuildsRequest
from api.responses.discord.get_guilds_response import GetGuildsResponse
from api.responses.error_response import ErrorResponse
from api.values import HTTPResponseCode
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, authentication_classes


@swagger_auto_schema(
    method='post',
    request_body=GetGuildsRequest.get_request_schema(),
    responses={
        HTTPResponseCode.ok: GetGuildsResponse.get_response_schema(),
        HTTPResponseCode.bad_request: ErrorResponse.get_response_schema(),
    },
)
@authentication_classes([BearerAuthentication])
@api_view(['POST'])
def get_guilds_view(request: WSGIRequest) -> JsonResponse:
    """
    Request to discord for user's guilds.

    Args:
        request: WSGIRequest
    Returns:
        JsonResponse
    """
    bearer_token = get_authorization_token(request.headers.get('Authorization'))

    if bearer_token is None:
        response = {
            'status': 'failure',
            'message': 'token required',
        }

        return JsonResponse(
            ErrorResponse.parse_obj(response).dict(),
            status=HTTPResponseCode.bad_request,
        )

    try:
        token_model = TokensModel.objects.get(token=bearer_token)
    except TokensModel.DoesNotExist:
        response = {
            'status': 'failure',
            'message': 'wrong token',
        }

        return JsonResponse(
            ErrorResponse.parse_obj(response).dict(),
            status=HTTPResponseCode.bad_request,
        )

    success, guilds = get_user_guilds(token_model.discord_token)

    if success is False:
        new_access_token = refresh_oauth2_credentials(token_model.discord_refresh_token)

        if new_access_token is None:
            response = {
                'status': 'failure',
                'message': 'token expired',
            }

            return JsonResponse(
                ErrorResponse.parse_obj(response).dict(),
                status=HTTPResponseCode.bad_request,
            )

        token_model.discord_token = new_access_token.access_token
        token_model.discord_refresh_token = new_access_token.refresh_token
        token_model.expires = datetime.now() + timedelta(
            seconds=new_access_token.expires_in,
        )

    response = {
        'status': 'success',
        'guilds': guilds,
    }

    return JsonResponse(
        GetGuildsResponse.parse_obj(response).dict(),
        status=HTTPResponseCode.ok,
    )
