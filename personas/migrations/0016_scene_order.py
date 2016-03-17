# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0015_auto_20150501_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='scene',
            name='order',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
