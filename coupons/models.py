from django.db import models
from account.models import Profile
from django.core.validators import MinValueValidator, \
                                   MaxValueValidator

class Coupon(models.Model):
	profiles = models.ManyToManyField(Profile)
	name = models.CharField(max_length=50)
	level = models.IntegerField()
	code = models.CharField(max_length=50,
	                        unique=True)
	valid_from = models.DateTimeField()
	valid_to = models.DateTimeField()
	discount = models.IntegerField(
	               validators=[MinValueValidator(0),
	                           MaxValueValidator(100)])
	active = models.BooleanField()

	def __str__(self):
	    return self.code