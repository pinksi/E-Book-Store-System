# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-15 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0020_cartbook_added_to_cart_bool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartbook',
            name='added_to_cart_bool',
            field=models.BooleanField(default=False),
        ),
    ]
