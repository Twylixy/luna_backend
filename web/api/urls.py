from api import views
from django.urls import path

urlpatterns = [
    path('', views.root_api_view),
]
