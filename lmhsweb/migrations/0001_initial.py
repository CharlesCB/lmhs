# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-17 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cote_auteur', models.CharField(blank=True, max_length=20, unique=True)),
                ('nom_auteur', models.CharField(blank=True, max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Auteur',
            },
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee_1re_publication', models.IntegerField(blank=True, max_length=4, null=True)),
                ('notice_id', models.TextField(blank=True, db_column='notice_ID', null=True)),
                ('annee_enregistrement', models.IntegerField(blank=True, max_length=4, null=True)),
                ('cote_calcul', models.TextField(blank=True, null=True, verbose_name='Cote')),
                ('annee_production', models.IntegerField(blank=True, max_length=4, null=True)),
                ('cote_calcul_url', models.TextField(blank=True, null=True)),
                ('auteur_old', models.CharField(blank=True, max_length=100, null=True)),
                ('cote_per_calcul', models.TextField(blank=True)),
                ('collection', models.CharField(blank=True, max_length=50)),
                ('tousindex_calcul', models.TextField(blank=True, db_column='tousIndex_calcul', null=True)),
                ('commentaire', models.TextField(blank=True)),
                ('cote_annee', models.IntegerField(max_length=4)),
                ('cote_auteur', models.CharField(max_length=50)),
                ('cote_numero', models.IntegerField(blank=True, null=True)),
                ('hash', models.BigIntegerField(blank=True, null=True)),
                ('cote_prefixe', models.CharField(max_length=20)),
                ('protection_droit_auteur', models.BooleanField(db_column='Protection_droit_auteur', default=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('date_fin', models.DateField(blank=True, null=True)),
                ('cal_support_enligne', models.TextField(blank=True, db_column='Cal_support_EnLigne')),
                ('depouillement', models.TextField(blank=True)),
                ('directeur_collection', models.CharField(blank=True, max_length=20)),
                ('directeur_publication', models.CharField(blank=True, max_length=20)),
                ('editeur', models.CharField(blank=True, max_length=20)),
                ('en_collection', models.CharField(blank=True, max_length=200)),
                ('fonds', models.CharField(blank=True, max_length=50)),
                ('genre', models.TextField(blank=True)),
                ('id_org', models.TextField(blank=True)),
                ('instrumentation', models.TextField(blank=True)),
                ('interprete', models.TextField(blank=True)),
                ('langue_origine', models.CharField(blank=True, max_length=20)),
                ('lieu', models.CharField(blank=True, max_length=50)),
                ('lieu_conservation', models.TextField(blank=True)),
                ('localisation', models.CharField(blank=True, max_length=200)),
                ('maison_edition', models.CharField(blank=True, max_length=50)),
                ('medium', models.TextField(blank=True)),
                ('methode_reproduction', models.TextField(blank=True)),
                ('mot_cle', models.CharField(blank=True, max_length=50)),
                ('nb_exemplaire', models.IntegerField(blank=True, null=True)),
                ('nb_page', models.CharField(blank=True, max_length=20)),
                ('nb_volume', models.CharField(blank=True, max_length=20)),
                ('no_page', models.CharField(blank=True, max_length=20)),
                ('no_volume', models.CharField(blank=True, max_length=20)),
                ('nom_org', models.TextField(blank=True)),
                ('organisme', models.TextField(blank=True, null=True)),
                ('projet', models.CharField(blank=True, max_length=200, null=True)),
                ('source', models.CharField(blank=True, max_length=200)),
                ('source_per', models.CharField(blank=True, max_length=200)),
                ('source_per_calcul', models.TextField(blank=True, null=True)),
                ('sujet', models.TextField(blank=True)),
                ('support', models.CharField(blank=True, max_length=200)),
                ('titre', models.CharField(blank=True, max_length=50)),
                ('traducteur', models.CharField(blank=True, max_length=50)),
                ('type', models.TextField()),
                ('type_evenement', models.TextField(blank=True)),
                ('cal_support_list_moins_enligne', models.TextField(blank=True, db_column='Cal_support_List_moins_EnLigne')),
                ('auteur', models.ManyToManyField(to='lmhsweb.Auteur')),
            ],
            options={
                'verbose_name': 'Principale',
            },
        ),
    ]
