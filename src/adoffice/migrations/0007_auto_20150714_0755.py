# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoffice', '0006_auto_20150714_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group_category',
            field=models.ManyToManyField(to='adoffice.GroupCategory', null=True, blank=True),
        ),
    ]
