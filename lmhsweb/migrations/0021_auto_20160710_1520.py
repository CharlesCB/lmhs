# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-10 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lmhsweb', '0020_auto_20160627_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lmhsweb.Collection'),
        ),
        migrations.AlterField(
            model_name='main',
            name='commentaire',
            field=models.TextField(blank=True, null=True),
        ),
    ]
