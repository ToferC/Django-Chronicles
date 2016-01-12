# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0049_mainmap_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='aspect',
            name='details',
            field=models.TextField(blank=True, null=True, help_text='Enter any additional details about your aspect here.'),
        ),
        migrations.AlterField(
            model_name='storyobject',
            name='c_type',
            field=models.CharField(choices=[('Faction', 'Faction'), ('Character', 'Character'), ('Creature', 'Creature'), ('Organization', 'Organization'), ('Place', 'Place'), ('Territory', 'Territory'), ('Thing', 'Thing')], default='Character', verbose_name='Story Object Type', max_length=32, help_text='Select a story object category.'),
        ),
    ]
