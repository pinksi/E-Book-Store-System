# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-16 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0025_auto_20160216_0233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartbook',
            name='added_to_cart_bool',
        ),
        migrations.AddField(
            model_name='cartbook',
            name='added_bookid',
            field=models.IntegerField(default=0),
        ),
    ]
