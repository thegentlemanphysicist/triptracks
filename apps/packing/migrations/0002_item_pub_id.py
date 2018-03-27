# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-25 06:55
from __future__ import unicode_literals

from django.db import migrations
import utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('packing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='pub_id',
            field=utils.fields.ShortUUIDField(default='9JV3yPdCxRdtvDqJVJDKRDy3', max_length=32),
        ),
    ]
