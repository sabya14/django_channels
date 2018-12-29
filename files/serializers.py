from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework import serializers

from .models import File


class FileSerializer(serializers.ModelSerializer):

	class Meta:
		model = File
		fields = "__all__"

	def create(self, validated_data):
		obj = File.objects.create(**validated_data)
		# Get the channel layer
		layer = get_channel_layer()
		# We identify the layer with the id of the group name, and fire an event to it
		async_to_sync(layer.group_send)('file_list', {
			'type': 'chat_message',
			'id': obj.id,
			'content': {'message': 'File Uploaded'}
		})
		return obj



