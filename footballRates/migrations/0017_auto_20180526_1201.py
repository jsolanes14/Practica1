# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-26 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footballRates', '0016_auto_20180526_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cronica',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='matchended',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='playervaloration',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]