from django.urls import path
from .consumers import TraderConsumer

websocket_urlpatterns = [
    path("wss/admin-dashboard/", TraderConsumer.as_asgi()),
]