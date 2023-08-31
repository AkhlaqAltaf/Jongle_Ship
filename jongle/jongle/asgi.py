"""
ASGI config for jongle project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from interface.consumers import NotificationConsumer
from django.urls import re_path 
from django.urls import path , include
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jongle.settings')

application = get_asgi_application()

ws_pattern = [
    re_path(r'ws/test/$', NotificationConsumer.as_asgi()),
    # re_path(r'/',  include('jongle.urls')),
]

# Use ProtocolTypeRouter to handle both HTTP and WebSocket protocols
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(ws_pattern),
})
