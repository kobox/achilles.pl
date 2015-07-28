# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoffice', '0017_auto_20150724_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='finishing',
            name='title_en',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='finishing',
            name='title_pl',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
