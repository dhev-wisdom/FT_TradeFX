import os

from channels.routing import ProtocolTypeRouter, URLRouter
import django
from tradeapp.consumers import TraderConsumer
from django.core.asgi import get_asgi_application
from django.urls import path
# import tradeapp.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tradeFX.settings')


django.setup()


application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/admin-dashboard/", TraderConsumer.as_asgi()),
        # tradeapp.routing.websocket_urlpatterns
    ]),
    "http": get_asgi_application(),
})
