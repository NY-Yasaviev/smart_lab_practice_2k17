# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 12:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0020_auto_20170717_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dates',
            name='practice',
        ),
        migrations.DeleteModel(
            name='Dates',
        ),
    ]
