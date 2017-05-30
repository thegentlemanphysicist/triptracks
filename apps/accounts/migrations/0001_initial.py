# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 00:03
from __future__ import unicode_literals

import django.contrib.auth.models
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('google_credentials', django.contrib.postgres.fields.jsonb.JSONField()),
                ('email', models.CharField(max_length=256, unique=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('pub_id', utils.fields.ShortUUIDField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
