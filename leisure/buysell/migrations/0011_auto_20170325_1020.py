# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buysell', '0010_auto_20170325_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellmodel',
            name='item_img',
            field=models.ImageField(upload_to='buysell/static/pictures'),
        ),
    ]
