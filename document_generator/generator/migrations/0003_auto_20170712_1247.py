# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('generator', '0002_auto_20170712_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='deanery',
            name='login',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='deanery',
            name='password',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='group_link',
            field=models.ManyToManyField(to='auth.Group'),
        ),
        migrations.AddField(
            model_name='student',
            name='login',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=16, null=True),
        ),
    ]