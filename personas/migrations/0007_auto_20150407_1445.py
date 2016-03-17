# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0006_auto_20150406_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='combat_info',
        ),
        migrations.AlterField(
            model_name='character',
            name='description',
            field=django_markdown.models.MarkdownField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.FloatField(default=50.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.FloatField(default=-1.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='skill',
            name='value',
            field=models.CharField(max_length=32, default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='statistic',
            name='value',
            field=models.CharField(max_length=32, default=0),
            preserve_default=True,
        ),
    ]
