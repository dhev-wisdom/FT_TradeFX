from django.urls import path
from .consumers import TraderConsumer

websocket_urlpatterns = [
    path("ws/admin-dashboard/", TraderConsumer.as_asgi()),
]