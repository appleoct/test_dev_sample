# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-16 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itest', '0025_taskmodel_lastrunningtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='lastRunningTime',
            field=models.CharField(max_length=100),
        ),
    ]