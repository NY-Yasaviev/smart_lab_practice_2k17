# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0013_auto_20170714_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practice',
            name='type',
            field=models.CharField(choices=[('Educational', 'Educational'), ('Factory', 'Factory'), ('Preddiplomnaya', 'Preddiplomnaya')], default='Educational', max_length=20),
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]