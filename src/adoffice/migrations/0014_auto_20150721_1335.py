# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoffice', '0013_auto_20150721_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupcategory',
            name='title_en',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='groupcategory',
            name='title_pl',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Opis', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_pl',
            field=models.TextField(null=True, verbose_name='Opis', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug_en',
            field=models.SlugField(max_length=150, unique=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug_pl',
            field=models.SlugField(max_length=150, unique=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title_en',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title_pl',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
