# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-30 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footballRates', '0007_auto_20180430_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pronostic',
            name='match',
        ),
        migrations.AddField(
            model_name='match',
            name='golslocal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='golsvisitant',
            field=models.IntegerField(default=0),
        ),
    ]
