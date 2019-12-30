# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-15 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0024_auto_20160216_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartbook',
            name='date_added_to_cart',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cartbook',
            name='date_purchased',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cartbook',
            name='purchased_bool',
            field=models.BooleanField(default=False),
        ),
    ]