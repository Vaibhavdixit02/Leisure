# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leisureactivities', '0002_remove_comments_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceToVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_page', models.CharField(max_length=1000)),
                ('link_img', models.CharField(max_length=1000)),
            ],
        ),
    ]
