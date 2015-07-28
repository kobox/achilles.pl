# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoffice', '0018_auto_20150724_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slogan',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slogan_en',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slogan_pl',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
    ]
