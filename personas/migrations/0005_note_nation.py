# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0004_auto_20150404_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='nation',
            field=models.ForeignKey(to='personas.Nation', blank=True, null=True),
            preserve_default=True,
        ),
    ]
