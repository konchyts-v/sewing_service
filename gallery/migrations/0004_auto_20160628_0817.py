# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-28 08:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20160628_0806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='width_field',
        ),
    ]
