from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from .models import File
from .serializers import FileSerializer


class FileListCreateView(ListCreateAPIView):
	permission_classes = [AllowAny]
	serializer_class = FileSerializer
	name = "files_list_create"
	queryset = File.objects.all()
