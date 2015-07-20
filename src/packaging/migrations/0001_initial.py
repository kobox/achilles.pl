# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_meta_title', models.CharField(help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title', blank=True)),
                ('meta_description', models.TextField(verbose_name='Description', blank=True)),
                ('keywords', models.CharField(max_length=500, null=True, blank=True)),
                ('slug', models.SlugField()),
                ('title', models.CharField(default=b'', max_length=254, verbose_name=b'Tytu\xc5\x82')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('description', models.TextField(null=True, verbose_name=b'Opis', blank=True)),
                ('picture', models.ImageField(default=b'pics/default.png', upload_to=b'pics/', verbose_name=b'Kategoria')),
                ('header', models.CharField(default=b'sec1', max_length=50, null=True, verbose_name=b'Klasa obrazka', blank=True)),
                ('order', models.IntegerField(default=0)),
                ('parent_category', models.ForeignKey(related_name='subcategories', blank=True, to='packaging.Category', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Finishing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='GroupCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_meta_title', models.CharField(help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title', blank=True)),
                ('meta_description', models.TextField(verbose_name='Description', blank=True)),
                ('keywords', models.CharField(max_length=500, null=True, blank=True)),
                ('title', models.CharField(max_length=254)),
                ('slug', models.SlugField(unique=True, max_length=150)),
                ('description', models.TextField(null=True, verbose_name=b'Opis', blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('format_size', models.CharField(max_length=10, blank=True)),
                ('picture', models.ImageField(default=b'pics/default.png', upload_to=b'pics/', verbose_name=b'Obrazek')),
                ('accessories', models.ManyToManyField(to='packaging.Accessories', null=True, blank=True)),
                ('category', models.ManyToManyField(to='packaging.Category', null=True, blank=True)),
                ('finishing', models.ManyToManyField(to='packaging.Finishing', null=True, blank=True)),
                ('group_category', models.ManyToManyField(to='packaging.GroupCategory', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(default=b'pics/default.png', upload_to=b'pics/', verbose_name=b'Product Image')),
                ('featured', models.BooleanField(default=False)),
                ('thumbnail', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(to='packaging.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Quota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(default=b'', max_length=254, verbose_name=b'Imi\xc4\x99 i Nazwisko')),
                ('company', models.CharField(default=b'', max_length=254, null=True, verbose_name=b'Firma', blank=True)),
                ('phone', models.CharField(default=b'', max_length=254, verbose_name=b'Telefon')),
                ('note', models.TextField(default=b'', null=True, verbose_name=b'Uwagi', blank=True)),
                ('newsletter', models.BooleanField(default=True, help_text=b'Chc\xc4\x99 by\xc4\x87 informowany o nowo\xc5\x9bciach i ofertach firmy Achilles.', verbose_name=b'Newsletter')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([('title', 'slug')]),
        ),
    ]
