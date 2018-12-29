from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from django.urls import path, include
from chat import routing as chat_routing
from files import routing as file_routing

application = ProtocolTypeRouter({
	# (http->django views is added by default)
	'websocket': AuthMiddlewareStack(
		URLRouter([
			path('chat_app/', URLRouter(chat_routing.websocket_urlpatterns)),
			path('file_app/', URLRouter(file_routing.websocket_urlpatterns)),
		])
	),
})
