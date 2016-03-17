# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0045_storyoptions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='background',
        ),
        migrations.RemoveField(
            model_name='story',
            name='map_tile',
        ),
        migrations.RemoveField(
            model_name='story',
            name='skill_type_name_1',
        ),
        migrations.RemoveField(
            model_name='story',
            name='skill_type_name_2',
        ),
        migrations.RemoveField(
            model_name='story',
            name='skill_type_name_3',
        ),
        migrations.RemoveField(
            model_name='story',
            name='skill_type_name_4',
        ),
        migrations.RemoveField(
            model_name='story',
            name='statistic_type_name_1',
        ),
        migrations.RemoveField(
            model_name='story',
            name='statistic_type_name_2',
        ),
        migrations.RemoveField(
            model_name='story',
            name='statistic_type_name_3',
        ),
        migrations.RemoveField(
            model_name='story',
            name='statistic_type_name_4',
        ),
        migrations.RemoveField(
            model_name='storyobject',
            name='combat_toggle',
        ),
        migrations.RemoveField(
            model_name='storyobject',
            name='equipment_toggle',
        ),
        migrations.RemoveField(
            model_name='storyobject',
            name='gallery_toggle',
        ),
        migrations.RemoveField(
            model_name='storyobject',
            name='gamestats_toggle',
        ),
        migrations.RemoveField(
            model_name='storyobject',
            name='skill_toggle',
        ),
        migrations.RemoveField(
            model_name='storyobject',
            name='social_toggle',
        ),
        migrations.RemoveField(
            model_name='storyobject',
            name='stats_toggle',
        ),
        migrations.RemoveField(
            model_name='storyoptions',
            name='colour_theme',
        ),
    ]
