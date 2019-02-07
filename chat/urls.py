# chat/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path('api/<str:room_name>/', views.api_room, name='api_room'),
]