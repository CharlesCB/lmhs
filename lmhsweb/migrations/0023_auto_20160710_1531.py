# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-10 15:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lmhsweb', '0022_auto_20160710_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main',
            name='city',
        ),
        migrations.RemoveField(
            model_name='main',
            name='country',
        ),
        migrations.RemoveField(
            model_name='main',
            name='state',
        ),
        migrations.AlterField(
            model_name='main',
            name='auteur',
            field=models.ManyToManyField(blank=True, null=True, to='lmhsweb.Auteur'),
        ),
        migrations.AlterField(
            model_name='main',
            name='directeur_publication',
            field=models.ManyToManyField(blank=True, null=True, to='lmhsweb.DirecteurPublication'),
        ),
        migrations.AlterField(
            model_name='main',
            name='editeur',
            field=models.ManyToManyField(blank=True, null=True, to='lmhsweb.Editeur'),
        ),
        migrations.AlterField(
            model_name='main',
            name='fonds',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lmhsweb.Fonds'),
        ),
        migrations.AlterField(
            model_name='main',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lmhsweb.Genre'),
        ),
        migrations.AlterField(
            model_name='main',
            name='localisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lmhsweb.Localisation'),
        ),
        migrations.AlterField(
            model_name='main',
            name='maison_edition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lmhsweb.MaisonEdition'),
        ),
        migrations.AlterField(
            model_name='main',
            name='medium',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lmhsweb.Medium'),
        ),
        migrations.AlterField(
            model_name='main',
            name='methode_reproduction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lmhsweb.MethodeReproduction'),
        ),
        migrations.AlterField(
            model_name='main',
            name='mot_cle',
            field=models.ManyToManyField(blank=True, null=True, to='lmhsweb.MotCle'),
        ),
        migrations.AlterField(
            model_name='main',
            name='nom_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lmhsweb.NomOrg'),
        ),
        migrations.AlterField(
            model_name='main',
            name='projet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lmhsweb.Projet'),
        ),
        migrations.AlterField(
            model_name='main',
            name='source',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='sujet',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='support',
            field=models.ManyToManyField(blank=True, null=True, to='lmhsweb.Support'),
        ),
        migrations.AlterField(
            model_name='main',
            name='traducteur',
            field=models.ManyToManyField(blank=True, null=True, to='lmhsweb.Traducteur'),
        ),
        migrations.AlterField(
            model_name='main',
            name='type_evenement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lmhsweb.TypeEvenement'),
        ),
    ]