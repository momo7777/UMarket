# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-14 15:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_used_stuff_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='used_stuff',
            name='created_time',
        ),
    ]