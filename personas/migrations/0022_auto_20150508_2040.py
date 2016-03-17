# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0021_auto_20150508_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='storyobject',
            name='combat_toggle',
            field=models.BooleanField(help_text='Check to enable combat info for this story object.', verbose_name='Enable Combat Info?', default=True),
        ),
        migrations.AddField(
            model_name='storyobject',
            name='gallery_toggle',
            field=models.BooleanField(help_text='Check to enable gallery images for this story object.', verbose_name='Enable Gallery Images?', default=True),
        ),
        migrations.AddField(
            model_name='storyobject',
            name='skill_toggle',
            field=models.BooleanField(help_text='Check to enable skills for this story object.', verbose_name='Enable Skills?', default=True),
        ),
        migrations.AddField(
            model_name='storyobject',
            name='social_toggle',
            field=models.BooleanField(help_text='Check to enable social functionality for this story object.', verbose_name='Enable Social Functions?', default=True),
        ),
        migrations.AddField(
            model_name='storyobject',
            name='stats_toggle',
            field=models.BooleanField(help_text='Check to enable statistics for this story object.', verbose_name='Enable Statistics?', default=True),
        ),
    ]
