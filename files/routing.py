# chat/routing.py
from django.urls import path

from . import consumers

websocket_urlpatterns = [
	path('file/<str:room_name>/', consumers.FileConsumer),
]
