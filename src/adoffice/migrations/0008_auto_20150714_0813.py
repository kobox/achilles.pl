# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoffice', '0007_auto_20150714_0755'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finishing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='finishing',
            field=models.ManyToManyField(to='adoffice.Finishing', null=True, blank=True),
        ),
    ]
