from __future__ import unicode_literals

from django.db import models

# Create your models here.


class About(models.Model):
	general_information = models.TextField(max_length=300)
	first_location = models.CharField(max_length=50)
	second_location = models.CharField(max_length=50)
	first_phone = models.CharField(max_length=15)
	second_phone = models.CharField(max_length=15)
	schedule_first = models.CharField(max_length=40)
	schedule_second = models.CharField(max_length=40)
	advantages = models.TextField(max_length=100)