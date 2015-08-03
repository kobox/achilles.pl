# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoffice', '0021_auto_20150730_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='title',
            field=models.CharField(default=b'', max_length=254),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='title',
            field=models.CharField(default=b'', max_length=254),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title',
            field=models.CharField(default=b'', max_length=254),
        ),
    ]
