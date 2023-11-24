from django.urls import re_path ,path

from .consumers import NotificationConsumer

websocket_urlpatterns = [
    path('ws/test/' , NotificationConsumer),
    re_path(r'ws/notifications/$', NotificationConsumer.as_asgi()),
]
