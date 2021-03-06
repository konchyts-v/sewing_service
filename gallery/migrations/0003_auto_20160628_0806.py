# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-28 08:06
from __future__ import unicode_literals

from django.db import migrations, models
import gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20160628_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='photo',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='photo',
            name='upload',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=gallery.models.upload_location, width_field='width_field'),
        ),
    ]
