# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoffice', '0005_product_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='format_size',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='group_category',
            field=models.ManyToManyField(related_name='groups', null=True, to='adoffice.GroupCategory', blank=True),
        ),
    ]
