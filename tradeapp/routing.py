from django.urls import path, re_path
from .consumers import TraderConsumer

websocket_urlpatterns = [
    path("ws/admin-dashboard/", TraderConsumer.as_asgi()),
]

# websocket_urlpatterns = [
#     re_path(r'ws/admin-dashboard/', TraderConsumer.as_asgi()),
#     re_path(r'ws/user-dashboard/', TraderConsumer.as_asgi()),
# ]