# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-10 16:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lmhsweb', '0025_auto_20160710_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='CotePrefixe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cote', models.CharField(blank=True, default=None, max_length=20, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Cote prefixe',
            },
        ),
        migrations.AlterField(
            model_name='main',
            name='cote_prefixe',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='lmhsweb.CotePrefixe'),
        ),
    ]
