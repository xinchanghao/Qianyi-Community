# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_user_user_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_sex',
            field=models.TextField(max_length=5, null=True, verbose_name='鎬у埆'),
        ),
    ]