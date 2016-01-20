# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoffice', '0029_auto_20160111_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='quota',
            name='ref',
            field=models.CharField(default=b'', max_length=254),
        ),
    ]
