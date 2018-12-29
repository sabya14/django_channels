from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework import serializers
from .models import File
from .consumers import FileConsumer

class FileSerializer(serializers.ModelSerializer):

	class Meta:
		model = File
		fields = "__all__"

	def create(self, validated_data):
		obj = File.objects.create(**validated_data)
		layer = get_channel_layer()
		async_to_sync(layer.group_send)('chat_file_list', {
			'type': 'chat_message',
			'content': {'message': 'File Uploaded'}
		})
		return obj



