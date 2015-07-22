# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoffice', '0014_auto_20150721_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='keywords_en',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='keywords_pl',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_description_en',
            field=models.TextField(null=True, verbose_name='Opis sekcji meta', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_description_pl',
            field=models.TextField(null=True, verbose_name='Opis sekcji meta', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='keywords_en',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='keywords_pl',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_description_en',
            field=models.TextField(null=True, verbose_name='Opis sekcji meta', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_description_pl',
            field=models.TextField(null=True, verbose_name='Opis sekcji meta', blank=True),
        ),
    ]
