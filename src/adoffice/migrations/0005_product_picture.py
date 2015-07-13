# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoffice', '0004_auto_20150713_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(default=b'pics/default.png', upload_to=b'pics/', verbose_name=b'Obrazek'),
        ),
    ]
