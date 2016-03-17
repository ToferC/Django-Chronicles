# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0008_auto_20150409_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='map_tile',
            field=models.CharField(max_length=128, default='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'),
            preserve_default=True,
        ),
    ]
