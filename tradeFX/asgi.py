import os

from channels.routing import ProtocolTypeRouter, URLRouter
from tradeapp.consumers import TraderConsumer
from django.core.asgi import get_asgi_application
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tradeFX.settings')



application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/admin-dashboard/", TraderConsumer.as_asgi()),
    ]),
    "http": get_asgi_application(),
})
