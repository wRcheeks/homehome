# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-08 14:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homehome', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='point',
            field=models.IntegerField(default=0, verbose_name='点数'),
        ),
        migrations.AlterField(
            model_name='task',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
    ]
