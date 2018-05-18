# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes_books', '0002_auto_20170815_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='liked_books',
        ),
        migrations.AddField(
            model_name='book',
            name='liked_users',
            field=models.ManyToManyField(related_name='liked_books', to='likes_books.User'),
        ),
    ]
