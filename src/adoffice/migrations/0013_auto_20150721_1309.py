# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoffice', '0012_auto_20150720_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Opis', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='description_pl',
            field=models.TextField(null=True, verbose_name='Opis', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug_en',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug_pl',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(default=b'', max_length=254, null=True, verbose_name='Tytu\u0142'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_pl',
            field=models.CharField(default=b'', max_length=254, null=True, verbose_name='Tytu\u0142'),
        ),
        migrations.AlterField(
            model_name='category',
            name='_meta_title',
            field=models.CharField(help_text='Opcjonalny HTML title tag.', max_length=500, null=True, verbose_name='Tytu\u0142 sekcji meta', blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='meta_description',
            field=models.TextField(verbose_name='Opis sekcji meta', blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(default=b'', max_length=254, verbose_name='Tytu\u0142'),
        ),
        migrations.AlterField(
            model_name='product',
            name='_meta_title',
            field=models.CharField(help_text='Opcjonalny HTML title tag.', max_length=500, null=True, verbose_name='Tytu\u0142 sekcji meta', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_description',
            field=models.TextField(verbose_name='Opis sekcji meta', blank=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='picture',
            field=models.ImageField(default=b'pics/default.png', upload_to=b'pics/', verbose_name='Obrazek'),
        ),
        migrations.AlterField(
            model_name='quota',
            name='full_name',
            field=models.CharField(default=b'', max_length=254, verbose_name='Imi\u0119 i Nazwisko'),
        ),
        migrations.AlterField(
            model_name='quota',
            name='newsletter',
            field=models.BooleanField(default=True, help_text='Chc\u0119 by\u0107 informowany o nowo\u015bciach i ofertach firmy Achilles.', verbose_name='Newsletter'),
        ),
    ]
