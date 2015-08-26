# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20150826_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='newsl',
            field=models.BooleanField(default=True, verbose_name='U'),
        ),
    ]
