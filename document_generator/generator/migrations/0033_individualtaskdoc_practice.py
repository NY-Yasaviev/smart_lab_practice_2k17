# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 11:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0032_auto_20170718_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='individualtaskdoc',
            name='practice',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='generator.Practice'),
        ),
    ]