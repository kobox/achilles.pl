# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoffice', '0003_auto_20150710_0700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='heroimage',
        ),
        migrations.AddField(
            model_name='category',
            name='header',
            field=models.CharField(default=b'sec1', max_length=50, null=True, verbose_name=b'Klasa obrazka', blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
