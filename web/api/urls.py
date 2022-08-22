from api.routes.auth.discord import auth_discord_view
from api.routes.discord.get_guilds import get_guilds_view
from api.routes.root import routes_root_view
from api.routes.status.healthcheck import test_healthcheck_view
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('', routes_root_view),
    path('docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'docs/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger',
    ),
    path('docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('status/healthcheck/', test_healthcheck_view),
    path('auth/discord/', auth_discord_view),
    path('discord/get_guilds/', get_guilds_view),
]
