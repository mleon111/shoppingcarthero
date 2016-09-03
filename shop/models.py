from django.db import models
from django.utils import timezone
from django.conf import settings
from PIL import Image
from io import StringIO

class Item(models.Model):
	DOLLAR = 'USD'
	SHOPCOIN = 'SHP'
	CURRENCY_CHOICES = (
		(DOLLAR, 'USD'),
		(SHOPCOIN, 'SHP'),
	)

	name = models.CharField(default='', max_length=200)
	description = models.TextField(default='')
	image = models.ImageField(default='items/no_image.png', upload_to='items/', blank=True)
	price = models.IntegerField(default=0)
	quantity = models.IntegerField(default=0)
	pub_date = models.DateTimeField(default=timezone.now)
	currency = models.CharField(
		max_length=3,
		choices=CURRENCY_CHOICES,
		default=DOLLAR,
	)

	def __str__(self):
		return self.name

	def is_usd(self):
		return self.currency in (self.DOLLAR)
