# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-26 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footballRates', '0013_auto_20180525_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pronostic',
            name='pronosticPartit',
            field=models.PositiveIntegerField(choices=[(1, '1 Local'), (2, 'X Empat'), (3, '2 Visitant')]),
        ),
    ]
