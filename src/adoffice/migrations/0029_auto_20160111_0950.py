# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoffice', '0028_auto_20150817_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='format_size',
            field=models.CharField(max_length=25, blank=True),
        ),
    ]
