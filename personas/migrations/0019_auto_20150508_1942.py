# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0018_auto_20150508_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='setting',
            field=models.CharField(default='Setting', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='story',
            name='themes',
            field=models.CharField(default='War, Exploration, Compassion', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storyobject',
            name='role',
            field=models.CharField(default='PC', max_length=256),
            preserve_default=False,
        ),
    ]
