# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buysell', '0008_auto_20170325_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellmodel',
            name='item_img',
            field=models.ImageField(upload_to='/buysell/static/pictures'),
        ),
    ]