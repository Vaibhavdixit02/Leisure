# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leisureactivities', '0005_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='event_date',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='events',
            name='event_time',
            field=models.CharField(max_length=10),
        ),
    ]
