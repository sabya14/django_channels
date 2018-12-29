from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path, include
from chat import routing

application = ProtocolTypeRouter({
	# (http->django views is added by default)
	'websocket': AuthMiddlewareStack(
		URLRouter(
			routing.websocket_urlpatterns
		)
	),
})
