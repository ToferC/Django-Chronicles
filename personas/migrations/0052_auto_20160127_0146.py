# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0051_auto_20160114_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainmap',
            name='zoom',
            field=models.IntegerField(default=6, help_text='Sets the default zoom for your map'),
        ),
        migrations.AddField(
            model_name='storyoptions',
            name='base_latitude',
            field=models.FloatField(default=50.0, blank=True),
        ),
        migrations.AddField(
            model_name='storyoptions',
            name='base_longitude',
            field=models.FloatField(default=-1.3, blank=True),
        ),
        migrations.AddField(
            model_name='storyoptions',
            name='zoom',
            field=models.IntegerField(default=6, help_text='Sets the default zoom for your map'),
        ),
    ]
