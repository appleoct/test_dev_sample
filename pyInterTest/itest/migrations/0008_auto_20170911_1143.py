# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-11 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itest', '0007_auto_20170811_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='publicAssertModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('value', models.TextField()),
                ('type', models.IntegerField(default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itest.Project')),
            ],
        ),
        migrations.RemoveField(
            model_name='datamodal',
            name='testCase',
        ),
        migrations.RemoveField(
            model_name='testcasedatamodel',
            name='testCase',
        ),
        migrations.RemoveField(
            model_name='testcasemodel',
            name='globalTestData',
        ),
        migrations.RemoveField(
            model_name='testcasemodel',
            name='module',
        ),
        migrations.RemoveField(
            model_name='testcasemodel',
            name='testDataList',
        ),
        migrations.AddField(
            model_name='testcasemodel',
            name='caseLabels',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='testcasemodel',
            name='headerData',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='testcasemodel',
            name='otherAssert',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='testcasemodel',
            name='parmasData',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='testcasemodel',
            name='postSql',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='testcasemodel',
            name='postTestCase',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='testcasemodel',
            name='preAssert',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='testcasemodel',
            name='preSql',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='testcasemodel',
            name='preTestCase',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='testcasemodel',
            name='dec',
            field=models.TextField(default=''),
        ),
        migrations.DeleteModel(
            name='dataModal',
        ),
        migrations.DeleteModel(
            name='TestCaseDataModel',
        ),
    ]
