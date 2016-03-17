# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0054_auto_20160129_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storyobject',
            name='c_type',
            field=models.CharField(choices=[('Faction', 'Faction'), ('Character', 'Character'), ('Creature', 'Creature'), ('Organization', 'Organization'), ('Territory', 'Territory'), ('Thing', 'Thing'), ('Event', 'Event')], verbose_name='Story Object Type', help_text='Select a story object category.', default='Character', max_length=32),
        ),
    ]
