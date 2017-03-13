# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-08 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('contents', models.TextField(blank=True, verbose_name='タスク内容')),
                ('point', models.IntegerField(blank=True, verbose_name='点数')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('is_completed', models.IntegerField(default=0)),
            ],
        ),
    ]