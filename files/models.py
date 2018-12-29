from django.db import models


class File(models.Model):
	ver = '1.0'

	name = models.CharField(max_length=999)
	file = models.FileField(null=False)

	def __str__(self):
		return self.name
