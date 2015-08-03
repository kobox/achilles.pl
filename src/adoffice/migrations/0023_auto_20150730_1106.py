# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoffice', '0022_auto_20150730_0719'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_meta_title', models.CharField(help_text='Opcjonalny HTML title tag.', max_length=500, null=True, verbose_name='Tytu\u0142 sekcji meta', blank=True)),
                ('meta_description', models.TextField(verbose_name='Opis sekcji meta', blank=True)),
                ('keywords', models.CharField(max_length=500, null=True, blank=True)),
                ('section1', models.TextField(null=True, verbose_name='Sekcja-1', blank=True)),
                ('section2', models.TextField(null=True, verbose_name='Sekcja-2', blank=True)),
                ('title', models.CharField(default=b'', max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PageClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'homepage', max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='AboutPage',
        ),
        migrations.DeleteModel(
            name='ContactPage',
        ),
        migrations.DeleteModel(
            name='HomePage',
        ),
        migrations.AddField(
            model_name='page',
            name='pageclass',
            field=models.ForeignKey(blank=True, to='adoffice.PageClass', null=True),
        ),
    ]
