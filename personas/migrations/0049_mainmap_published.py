# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0048_place_main_map'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainmap',
            name='published',
            field=models.BooleanField(default=True, help_text='Elements that are NOT published will only be viewable in your Workshop.'),
        ),
    ]
