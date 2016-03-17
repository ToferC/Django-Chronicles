# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0037_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameStats',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('content', django_markdown.models.MarkdownField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='storyobject',
            name='gamestats_toggle',
            field=models.BooleanField(default=True, verbose_name='Enable Game Stats field?', help_text='Check to enable a markdown field for entering game statistics.\n        This is the default option, but you can choose specific tabbed fields below if you prefer.'),
        ),
        migrations.AlterField(
            model_name='storyobject',
            name='combat_toggle',
            field=models.BooleanField(default=False, verbose_name='Enable Combat Info?', help_text='Check to enable combat info for this story object.'),
        ),
        migrations.AlterField(
            model_name='storyobject',
            name='equipment_toggle',
            field=models.BooleanField(default=False, verbose_name='Enable Equipment?', help_text='Check to enable equipment for this story object.'),
        ),
        migrations.AlterField(
            model_name='storyobject',
            name='gallery_toggle',
            field=models.BooleanField(default=False, verbose_name='Enable Gallery Images?', help_text='Check to enable gallery images for this story object.'),
        ),
        migrations.AlterField(
            model_name='storyobject',
            name='skill_toggle',
            field=models.BooleanField(default=False, verbose_name='Enable Skills?', help_text='Check to enable skills for this story object.'),
        ),
        migrations.AlterField(
            model_name='storyobject',
            name='social_toggle',
            field=models.BooleanField(default=False, verbose_name='Enable Social Functions?', help_text='Check to enable social functionality for this story object.'),
        ),
        migrations.AlterField(
            model_name='storyobject',
            name='stats_toggle',
            field=models.BooleanField(default=False, verbose_name='Enable Statistics?', help_text='Check to enable statistics for this story object.'),
        ),
        migrations.AddField(
            model_name='gamestats',
            name='storyobject',
            field=models.ForeignKey(to='personas.StoryObject'),
        ),
    ]
