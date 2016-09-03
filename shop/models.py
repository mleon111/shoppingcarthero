from django.db import models
from django.utils import timezone
from django.conf import settings
from PIL import Image
from io import StringIO


class Item(models.Model):
	name = models.CharField(max_length=200)
	price = models.IntegerField(default=0)
	quantity = models.IntegerField(default=0)
	image = models.ImageField(upload_to='items/', blank=True)
	pub_date = models.DateTimeField(default=timezone.now)


	def __str__(self):
		return self.name
