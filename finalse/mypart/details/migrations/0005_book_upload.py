# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-12 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0004_book_clicks'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='upload',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]
