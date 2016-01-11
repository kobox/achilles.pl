# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_profile_newsl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='newsl',
            field=models.BooleanField(default=True, verbose_name='Us\u0142ugi dla Poligrafii'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(upload_to='profile_pics/%Y-%m-%d/', null=True, verbose_name='Moje logo', blank=True),
        ),
    ]
