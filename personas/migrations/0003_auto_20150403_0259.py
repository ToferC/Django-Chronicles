# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_auto_20150403_0230'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='statistic_type_name_1',
            field=models.CharField(default='Physical', max_length=24),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='statistic_type_name_2',
            field=models.CharField(default='Mental', max_length=24),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='statistic_type_name_3',
            field=models.CharField(default='Social', max_length=24),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='statistic_type_name_4',
            field=models.CharField(default='Magic', max_length=24),
            preserve_default=True,
        ),
    ]
