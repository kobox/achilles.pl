# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('title', models.CharField(default=b'', max_length=254, verbose_name=b'Tytu\xc5\x82')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('description', models.TextField(null=True, verbose_name=b'Opis', blank=True)),
                ('picture', models.ImageField(default=b'pics/default.png', upload_to=b'pics/', verbose_name=b'Kategoria')),
                ('heroimage', models.ImageField(default=b'pics/default.png', upload_to=b'pics/', verbose_name=b'Hero Image')),
                ('order', models.IntegerField(default=0, max_length=3)),
                ('parent_category', models.ForeignKey(related_name='subcategories', blank=True, to='adoffice.Category', null=True)),
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
                ('title', models.CharField(max_length=254)),
                ('slug', models.SlugField(unique=True, max_length=150)),
                ('description', models.TextField(null=True, verbose_name=b'Opis', blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('category', models.ManyToManyField(to='adoffice.Category', null=True, blank=True)),
                ('group_category', models.ManyToManyField(to='adoffice.GroupCategory', null=True, blank=True)),
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
                ('product', models.ForeignKey(to='adoffice.Product')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([('title', 'slug')]),
        ),
    ]
