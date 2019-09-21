from channels.routing import ProtocolTypeRouter, URLRouter
from one import routing as r_one

application = ProtocolTypeRouter({
    'websocket': URLRouter(
        r_one.websocket_urlpatterns
    )
})