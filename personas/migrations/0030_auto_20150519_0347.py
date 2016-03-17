# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0029_auto_20150516_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='relationship_class',
            field=models.CharField(help_text='Enter the type of relationship here. E.g.: Ally, Friend, Lover, etc.', verbose_name='Relationship Description', default='Ally', max_length=32),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='relationship_description',
            field=models.CharField(verbose_name='Details', help_text='Enter any additional details here.', max_length=128),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='to_storyobject',
            field=models.ForeignKey(verbose_name='Object of Relationship', to='personas.StoryObject', help_text='Enter the character or story object subject of the relationship here.', related_name='to_storyobject'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='weight',
            field=models.CharField(help_text='If your story uses it, enter a numerical rating here.', verbose_name='Numerical Rating', default='50', max_length=64),
        ),
        migrations.AlterField(
            model_name='storyobject',
            name='c_type',
            field=models.CharField(help_text='Select a story object category.', verbose_name='Story Object Type', default='Character', max_length=32, choices=[('Abstract', 'Abstract'), ('Character', 'Character'), ('Creature', 'Creature'), ('Organization', 'Organization'), ('Thing', 'Thing')]),
        ),
    ]
