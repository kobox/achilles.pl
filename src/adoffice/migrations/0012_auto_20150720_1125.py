# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoffice', '0011_auto_20150720_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='segment',
            field=models.ForeignKey(default=b'1', to='adoffice.Segment'),
        ),
    ]
