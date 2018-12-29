from django.contrib import admin
from django.urls import path
from . import views

app_name = 'files'

urlpatterns = [
	# Related to generation
	path(
		'',
		views.FileListCreateView.as_view(),
		name=views.FileListCreateView.name
	),

]
