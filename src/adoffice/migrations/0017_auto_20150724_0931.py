# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoffice', '0016_product_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slogan',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='category',
            name='slogan_en',
            field=models.CharField(default=b'', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slogan_pl',
            field=models.CharField(default=b'', max_length=255, null=True),
        ),
    ]
