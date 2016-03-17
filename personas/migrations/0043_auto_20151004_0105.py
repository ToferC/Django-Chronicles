# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0042_auto_20150928_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storyobject',
            name='c_type',
            field=models.CharField(verbose_name='Story Object Type', choices=[('Faction', 'Faction'), ('Character', 'Character'), ('Creature', 'Creature'), ('Organization', 'Organization'), ('Place', 'Place'), ('Thing', 'Thing')], max_length=32, default='Character', help_text='Select a story object category.'),
        ),
    ]
