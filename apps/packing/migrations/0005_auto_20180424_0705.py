# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-24 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packing', '0004_packinglist_pub_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packinglistitem',
            name='name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='packinglistitem',
            name='original_name',
            field=models.CharField(max_length=256),
        ),
    ]
