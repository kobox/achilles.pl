# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoffice', '0023_auto_20150730_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='section1_en',
            field=models.TextField(null=True, verbose_name='Sekcja-1', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='section1_pl',
            field=models.TextField(null=True, verbose_name='Sekcja-1', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='section2_en',
            field=models.TextField(null=True, verbose_name='Sekcja-2', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='section2_pl',
            field=models.TextField(null=True, verbose_name='Sekcja-2', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='title_en',
            field=models.CharField(default=b'', max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='title_pl',
            field=models.CharField(default=b'', max_length=254, null=True),
        ),
    ]
