# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-15 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_auto_20160215_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartbook',
            name='is_purchased',
            field=models.NullBooleanField(),
        ),
    ]
