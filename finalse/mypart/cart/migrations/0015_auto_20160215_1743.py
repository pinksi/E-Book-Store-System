# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-15 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0014_auto_20160215_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartbook',
            name='purchase_bool',
            field=models.BooleanField(default=None),
        ),
    ]
