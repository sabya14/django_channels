from __future__ import absolute_import, unicode_literals

import threading

from asgiref.sync import async_to_sync, AsyncToSync
from celery import task, shared_task
from channels.layers import get_channel_layer


@shared_task
def activate_file():
	def sender(room_name, message):
		channel_layer = get_channel_layer()

		AsyncToSync(channel_layer.group_send)('file_list', {
			'type': 'chat_message',
			'content': {'message': 'File Uploaded'}
		})

	thread = threading.Thread(target=sender, args=('file_list', 'asdads'))
	thread.start()
	thread.join()
	print("Hello")
	# # Get the channel layer
	# layer = get_channel_layer()
	# async_to_sync(layer.group_send)('file_list', {
	# 	'type': 'chat_message',
	# 	'content': {'message': 'File Uploaded'}
	# })
	return
