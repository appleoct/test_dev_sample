# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 16:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itest', '0006_auto_20170811_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='expireData',
            new_name='expireDate',
        ),
    ]