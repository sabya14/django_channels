# http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channels_demo.settings')

app = Celery('channels_demo')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
