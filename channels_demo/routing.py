from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from files import routing as file_routing

application = ProtocolTypeRouter({
	# (http->django views is added by default)
	'websocket': AuthMiddlewareStack(
		URLRouter([
			# we can add for routers here
			path('file_app/', URLRouter(file_routing.websocket_urlpatterns)),
		])
	),
})
