# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-15 18:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_used_stuff_created_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='used_stuff',
            name='location',
            field=models.CharField(default=datetime.datetime(2016, 7, 15, 18, 51, 21, 83893, tzinfo=utc), max_length=225),
            preserve_default=False,
        ),
    ]
