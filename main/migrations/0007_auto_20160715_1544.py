# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-15 22:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_used_stuff_purchased_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='used_stuff',
            name='category',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='used_stuff',
            name='source',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
