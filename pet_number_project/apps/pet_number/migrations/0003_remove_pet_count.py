# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-24 20:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet_number', '0002_pet_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='count',
        ),
    ]
