# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoffice', '0026_category_items_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='items_title_en',
            field=models.CharField(default=b'', max_length=254, null=True, verbose_name='Tytu\u0142 Katalogu', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='items_title_pl',
            field=models.CharField(default=b'', max_length=254, null=True, verbose_name='Tytu\u0142 Katalogu', blank=True),
        ),
    ]
