# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-15 20:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0023_remove_cartbook_date_added_to_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartbook',
            name='date_added_to_cart',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='cartbook',
            name='date_purchased',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='cartbook',
            name='added_to_cart_bool',
            field=models.BooleanField(default=0),
        ),
    ]