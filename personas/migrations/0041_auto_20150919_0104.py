# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0040_auto_20150919_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storyobject',
            name='c_type',
            field=models.CharField(verbose_name='Story Object Type', choices=[('Force', 'Force'), ('Character', 'Character'), ('Creature', 'Creature'), ('Organization', 'Organization'), ('Place', 'Place'), ('Thing', 'Thing')], default='Character', max_length=32, help_text='Select a story object category.'),
        ),
    ]
