from django.urls import URLPattern, re_path
from . import consumers

websocket_urlpatter=[
    re_path(r'', consumers.ChatConsumer.as_asgi()),
]