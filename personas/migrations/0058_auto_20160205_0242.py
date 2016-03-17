# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0057_auto_20160201_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storyobject',
            name='c_type',
            field=models.CharField(max_length=32, help_text='Select a story object category.', default='Character', verbose_name='Story Object Type', choices=[('Faction', 'Faction'), ('Character', 'Character'), ('Creature', 'Creature'), ('Organization', 'Organization'), ('Place', 'Place'), ('Territory', 'Territory'), ('Thing', 'Thing'), ('Event', 'Event')]),
        ),
    ]
