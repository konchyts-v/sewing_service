# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-29 14:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_auto_20160629_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='photo',
            new_name='image',
        ),
    ]
