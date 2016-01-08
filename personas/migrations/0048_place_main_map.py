# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0047_auto_20151107_0332'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='main_map',
            field=models.ForeignKey(to='personas.MainMap', verbose_name='Map', null=True, blank=True, help_text='Leave this blank for the default map, or choose from the list.'),
        ),
    ]
