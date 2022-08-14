import os

from api.routes.auth.discord import auth_discord_view
from api.routes.root import routes_root_view
from api.routes.status.healthcheck import test_healthcheck_view
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='Luna API',
        default_version='beta',
        description="Luna's bot API",
        contact=openapi.Contact(email=os.getenv('SWAGGER_CONTACT_EMAIL')),
        license=openapi.License(name='BSD License'),
    ),
    url=os.getenv('SWAGGER_URL'),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', routes_root_view),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('status/healthcheck/', test_healthcheck_view),
    path('auth/discord/', auth_discord_view),
]
