# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leisureactivities', '0007_auto_20170313_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='user_name',
            field=models.CharField(default='vaibhav', max_length=100),
        ),
        migrations.AddField(
            model_name='placetoeat',
            name='user_name',
            field=models.CharField(default='vaibhav', max_length=100),
        ),
        migrations.AddField(
            model_name='placetovisit',
            name='user_name',
            field=models.CharField(default='vaibhav', max_length=100),
        ),
    ]
