# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0056_auto_20160201_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainmap',
            name='base_latitude',
            field=models.FloatField(blank=True, default=50.0),
        ),
        migrations.AlterField(
            model_name='mainmap',
            name='base_longitude',
            field=models.FloatField(blank=True, default=-0.15),
        ),
    ]
