# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-10 16:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lmhsweb', '0026_auto_20160710_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='langue_origine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lmhsweb.LangueOrigine'),
        ),
    ]
