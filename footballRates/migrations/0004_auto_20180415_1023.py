# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-15 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footballRates', '0003_auto_20180415_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='age',
        ),
        migrations.RemoveField(
            model_name='player',
            name='name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='number',
        ),
        migrations.RemoveField(
            model_name='player',
            name='team',
        ),
        migrations.AddField(
            model_name='player',
            name='dorsal',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='player',
            name='edat',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='player',
            name='equip',
            field=models.TextField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='player',
            name='nacionalitat',
            field=models.TextField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='player',
            name='nom',
            field=models.TextField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='player',
            name='posicio',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Porter'), (2, 'Defensa'), (3, 'Migcampista'), (4, 'Davanter')], default=3, verbose_name='Posicio (principal)'),
        ),
    ]
