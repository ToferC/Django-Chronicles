# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0034_auto_20150712_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='nation',
            field=models.ForeignKey(null=True, blank=True, to='personas.Nation'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='from_storyobject',
            field=models.ForeignKey(to='personas.StoryObject', verbose_name='Source of Relationship', related_name='from_storyobject'),
        ),
        migrations.AlterField(
            model_name='story',
            name='colour_theme',
            field=models.CharField(max_length=12, choices=[('Light', 'Light'), ('Dark', 'Dark')], default='Dark', help_text='Please note that the LIGHT field is not yet optimized.'),
        ),
        migrations.AlterField(
            model_name='story',
            name='map_tile',
            field=models.CharField(max_length=128, default='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', help_text="This field is used for Leaflet maps in the engine.\n        The default tile set is openstreetmap.\n        You probably shouldn't touch this unless you have another tileset in mind."),
        ),
        migrations.AlterField(
            model_name='story',
            name='skill_type_name_1',
            field=models.CharField(max_length=24, default='General', blank=True, help_text='This field and the skill fields below set the name for different skill types in a game.\n        They are optional, but if you are using skills of some kind, the first value should be set.'),
        ),
        migrations.AlterField(
            model_name='story',
            name='statistic_type_name_1',
            field=models.CharField(max_length=24, default='Physical', blank=True, help_text='This field and the statistic fields below set the name for different stat types in a game.\n        They are optional, but if you are using statistics of some kind, the first value should be set.'),
        ),
        migrations.AlterField(
            model_name='story',
            name='themes',
            field=models.CharField(max_length=256, help_text='Enter the themes for your story here.'),
        ),
    ]
