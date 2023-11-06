# isort: skip_file
from django.core.asgi import get_asgi_application

django_asgi_app = get_asgi_application()

import os
import django

django.setup()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from tradeapp.consumers import TraderConsumer
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tradeFX.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"



application = ProtocolTypeRouter({
    "https": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("wss/admin-dashboard/", TraderConsumer.as_asgi()),
            # tradeapp.routing.websocket_urlpatterns
    ]),
    ),
})
