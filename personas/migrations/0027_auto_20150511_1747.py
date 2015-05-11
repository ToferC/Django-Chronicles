# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0026_auto_20150511_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scratchpad',
            name='content',
            field=models.TextField(),
        ),
    ]
