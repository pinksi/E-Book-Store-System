# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-15 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_cartbook_have_purchased'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartbook',
            name='have_purchased',
            field=models.NullBooleanField(),
        ),
    ]
