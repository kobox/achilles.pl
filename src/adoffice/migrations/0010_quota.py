# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoffice', '0009_auto_20150714_0825'),
    ]

    operations = [
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
    ]
