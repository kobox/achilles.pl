# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoffice', '0010_quota'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='_meta_title',
            field=models.CharField(help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='keywords',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_description',
            field=models.TextField(verbose_name='Description', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='_meta_title',
            field=models.CharField(help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='keywords',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_description',
            field=models.TextField(verbose_name='Description', blank=True),
        ),
    ]
