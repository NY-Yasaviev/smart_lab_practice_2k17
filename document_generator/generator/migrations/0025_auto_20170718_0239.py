# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0024_auto_20170718_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individualtask',
            name='dateFrom',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='individualtask',
            name='dateTo',
            field=models.DateField(blank=True, null=True),
        ),
    ]