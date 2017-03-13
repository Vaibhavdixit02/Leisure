# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leisureactivities', '0004_placetoeat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateField()),
                ('event_time', models.TimeField()),
                ('event_place', models.CharField(max_length=500)),
                ('event_desc', models.CharField(max_length=1000)),
            ],
        ),
    ]