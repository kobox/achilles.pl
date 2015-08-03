# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoffice', '0020_auto_20150728_0801'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_meta_title', models.CharField(help_text='Opcjonalny HTML title tag.', max_length=500, null=True, verbose_name='Tytu\u0142 sekcji meta', blank=True)),
                ('meta_description', models.TextField(verbose_name='Opis sekcji meta', blank=True)),
                ('keywords', models.CharField(max_length=500, null=True, blank=True)),
                ('section1', models.TextField(null=True, verbose_name='Sekcja-1', blank=True)),
                ('section2', models.TextField(null=True, verbose_name='Sekcja-2', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_meta_title', models.CharField(help_text='Opcjonalny HTML title tag.', max_length=500, null=True, verbose_name='Tytu\u0142 sekcji meta', blank=True)),
                ('meta_description', models.TextField(verbose_name='Opis sekcji meta', blank=True)),
                ('keywords', models.CharField(max_length=500, null=True, blank=True)),
                ('section1', models.TextField(null=True, verbose_name='Sekcja-1', blank=True)),
                ('section2', models.TextField(null=True, verbose_name='Sekcja-2', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_meta_title', models.CharField(help_text='Opcjonalny HTML title tag.', max_length=500, null=True, verbose_name='Tytu\u0142 sekcji meta', blank=True)),
                ('meta_description', models.TextField(verbose_name='Opis sekcji meta', blank=True)),
                ('keywords', models.CharField(max_length=500, null=True, blank=True)),
                ('section1', models.TextField(null=True, verbose_name='Sekcja-1', blank=True)),
                ('section2', models.TextField(null=True, verbose_name='Sekcja-2', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='quota',
            name='note',
            field=models.TextField(default=b'', null=True, verbose_name='Wiadomo\u015b\u0107', blank=True),
        ),
    ]
