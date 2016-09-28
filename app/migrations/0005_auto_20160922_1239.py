# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='鍐呭\ue190'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='鍙戝竷鏃堕棿'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=256, verbose_name='鏍囬\ue57d'),
        ),
        migrations.AlterField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='鏇存柊鏃堕棿'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='birth_time',
            field=models.DateTimeField(verbose_name='鍑虹敓骞存湀'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='info',
            field=models.TextField(verbose_name='绠�浠�'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='name',
            field=models.CharField(max_length=256, verbose_name='濮撳悕'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='sex',
            field=models.CharField(max_length=5, verbose_name='鎬у埆'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='鏇存柊鏃堕棿'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_addr',
            field=models.TextField(verbose_name='绠�浠�'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_birth',
            field=models.DateTimeField(verbose_name='鍑虹敓骞存湀'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_email',
            field=models.CharField(max_length=256, verbose_name='閭\ue1be\ue188'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=256, verbose_name='濮撳悕'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_password',
            field=models.CharField(max_length=16, verbose_name='瀵嗙爜'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_sex',
            field=models.CharField(max_length=5, verbose_name='鎬у埆'),
        ),
    ]