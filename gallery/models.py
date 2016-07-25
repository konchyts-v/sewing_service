from __future__ import unicode_literals

from django.db import models

# Create your models here.

def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)

class Photo(models.Model):
	image = models.ImageField()
	