# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-14 20:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lmhsweb', '0027_auto_20160710_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDFFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_file', models.FileField(upload_to='PDF')),
                ('pdf_text', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='main',
            name='cote_annee',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='cote_numero',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='editeur',
            field=models.ManyToManyField(blank=True, null=True, to='lmhsweb.Editeur', verbose_name='\xc9diteur'),
        ),
        migrations.AlterField(
            model_name='main',
            name='fonds',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lmhsweb.Fonds', verbose_name='Fonds'),
        ),
        migrations.AlterField(
            model_name='main',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lmhsweb.Genre', verbose_name='Genre'),
        ),
        migrations.AddField(
            model_name='pdffile',
            name='notice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pdfs', to='lmhsweb.Main'),
        ),
    ]
