# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leisureactivities', '0006_auto_20170313_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='event_date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='events',
            name='event_time',
            field=models.CharField(max_length=100),
        ),
    ]
