# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0055_auto_20160201_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storyobject',
            name='slug',
            field=models.SlugField(unique=True, max_length=255),
        ),
    ]
