# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-25 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmhsweb', '0038_auto_20161025_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='nom',
            field=models.CharField(max_length=200),
        ),
    ]
