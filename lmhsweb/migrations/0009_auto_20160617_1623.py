# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-17 16:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lmhsweb', '0008_auto_20160617_0455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auteur',
            old_name='cote_auteur',
            new_name='cote',
        ),
        migrations.RenameField(
            model_name='auteur',
            old_name='nom_auteur',
            new_name='nom',
        ),
    ]
