# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-20 03:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_gold', '0002_auto_20170818_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]
