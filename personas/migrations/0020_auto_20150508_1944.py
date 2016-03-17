# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0019_auto_20150508_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storyobject',
            name='age',
        ),
        migrations.RemoveField(
            model_name='storyobject',
            name='birthplace',
        ),
        migrations.RemoveField(
            model_name='storyobject',
            name='xp',
        ),
    ]
