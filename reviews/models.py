from __future__ import unicode_literals

from django.db import models
 # -- coding: utf-8 --
# Create your models here.

class Reviews(models.Model):
	sender_name = models.CharField(max_length=20)
	message = models.TextField(max_length=200)
	pub_date = models.DateTimeField()