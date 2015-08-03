# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoffice', '0024_auto_20150730_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='pageclass',
            field=models.ForeignKey(default=b'1', to='adoffice.PageClass'),
        ),
    ]
