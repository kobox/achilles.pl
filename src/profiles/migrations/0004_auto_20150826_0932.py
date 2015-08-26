# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20150826_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='newsp',
            field=models.BooleanField(default=True, verbose_name='Opakowania i materia\u0142y POS'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.BooleanField(default=True, verbose_name='Artyku\u0142y Reklamowe'),
        ),
    ]
