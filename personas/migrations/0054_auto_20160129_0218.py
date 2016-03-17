# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0053_place_zoom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storyobject',
            name='c_type',
            field=models.CharField(help_text='Select a story object category.', choices=[('Faction', 'Faction'), ('Character', 'Character'), ('Creature', 'Creature'), ('Organization', 'Organization'), ('Place', 'Place'), ('Territory', 'Territory'), ('Thing', 'Thing'), ('Event', 'Event')], verbose_name='Story Object Type', max_length=32, default='Character'),
        ),
    ]
