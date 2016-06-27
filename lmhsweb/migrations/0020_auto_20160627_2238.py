# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-27 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmhsweb', '0019_auto_20160627_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='depouillement',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='instrumentation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='interprete',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='lieu',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Lieu'),
        ),
        migrations.AlterField(
            model_name='main',
            name='notice_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='titre',
            field=models.CharField(max_length=100),
        ),
    ]
