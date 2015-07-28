# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email_verified',
            field=models.BooleanField(default=False, verbose_name='Email zweryfikowany'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(upload_to='profile_pics/%Y-%m-%d/', null=True, verbose_name='Twoje logo', blank=True),
        ),
    ]
