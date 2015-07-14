# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoffice', '0008_auto_20150714_0813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='accessories',
            field=models.ManyToManyField(to='adoffice.Accessories', null=True, blank=True),
        ),
    ]
