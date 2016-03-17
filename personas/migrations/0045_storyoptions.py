# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0044_auto_20151007_0233'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryOptions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('colour_theme', models.CharField(default='Dark', choices=[('Light', 'Light'), ('Dark', 'Dark')], help_text='Please note that the LIGHT field is not yet optimized.', max_length=12)),
                ('map_tile', models.CharField(default='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', help_text="This field is used for Leaflet maps in the engine.\n        The default tile set is openstreetmap.\n        You probably shouldn't touch this unless you have another tileset in mind.", max_length=128)),
                ('skill_type_name_1', models.CharField(blank=True, default='General', help_text='This field and the skill fields below set the name for different skill types in a game.\n        They are optional, but if you are using skills of some kind, the first value should be set.', max_length=24)),
                ('skill_type_name_2', models.CharField(blank=True, default='Investigative', max_length=24)),
                ('skill_type_name_3', models.CharField(blank=True, default='Combat', max_length=24)),
                ('skill_type_name_4', models.CharField(blank=True, default='Knowledge', max_length=24)),
                ('statistic_type_name_1', models.CharField(blank=True, default='Physical', help_text='This field and the statistic fields below set the name for different stat types in a game.\n        They are optional, but if you are using statistics of some kind, the first value should be set.', max_length=24)),
                ('statistic_type_name_2', models.CharField(blank=True, default='Mental', max_length=24)),
                ('statistic_type_name_3', models.CharField(blank=True, default='Social', max_length=24)),
                ('statistic_type_name_4', models.CharField(blank=True, default='Magic', max_length=24)),
                ('gamestats_toggle', models.BooleanField(verbose_name='Enable Game Stats field?', default=True, help_text='Check to enable a markdown field for entering game statistics.\n        This is the default option, but you can choose specific tabbed fields below if you prefer.')),
                ('stats_toggle', models.BooleanField(verbose_name='Enable Statistics?', default=False, help_text='Check to enable statistics for this story object.')),
                ('skill_toggle', models.BooleanField(verbose_name='Enable Skills?', default=False, help_text='Check to enable skills for this story object.')),
                ('combat_toggle', models.BooleanField(verbose_name='Enable Combat Info?', default=False, help_text='Check to enable combat info for this story object.')),
                ('equipment_toggle', models.BooleanField(verbose_name='Enable Equipment?', default=False, help_text='Check to enable equipment for this story object.')),
                ('gallery_toggle', models.BooleanField(verbose_name='Enable Gallery Images?', default=False, help_text='Check to enable gallery images for this story object.')),
                ('social_toggle', models.BooleanField(verbose_name='Enable Social Functions?', default=False, help_text='Check to enable social functionality for this story object.')),
                ('story', models.ForeignKey(to='personas.Story')),
            ],
        ),
    ]
