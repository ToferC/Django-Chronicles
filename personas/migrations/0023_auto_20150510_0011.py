# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0022_auto_20150508_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='date_joined',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='from_storyobject',
            field=models.ForeignKey(to='personas.StoryObject', verbose_name='Subject of Relationship', related_name='from_storyobject'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='relationship_class',
            field=models.CharField(verbose_name='Defining Emotion', choices=[('Ally', 'Ally'), ('Enemy', 'Enemy'), ('Friend', 'Friend'), ('Spouse', 'Spouse'), ('Parent', 'Parent'), ('Child', 'Child'), ('Sibling', 'Sibling'), ('Rival', 'Rival'), ('Lover', 'Lover'), ('Partner', 'Business Partner'), ('Member', 'Co-member'), ('Owner', 'Owner'), ('Loves', 'Loves'), ('Hates', 'Hates'), ('Fears', 'Fears'), ('Envies', 'Envies'), ('Distrusts', 'Distrusts'), ('Trusts', 'Trusts'), ('Desires', 'Desires'), ('Respects', 'Respects'), ('Dislikes', 'Dislikes'), ('Is disgusted by', 'Is disgusted by'), ('Is angry at', 'Is angry at'), ('Is jealous of', 'Is jealous of'), ('Resents', 'Resents'), ('Is proud of', 'Is proud of'), ('Worships', 'Worships'), ('Reveres', 'Reveres'), ('Owns', 'Owns'), ('Belongs to', 'Belongs to'), ('Crews', 'Crews')], max_length=32, default='Ally'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='to_storyobject',
            field=models.ForeignKey(to='personas.StoryObject', verbose_name='Object of Relationship', related_name='to_storyobject'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='weight',
            field=models.CharField(verbose_name='Strength of the relationship', max_length=64, default='50'),
        ),
        migrations.AlterField(
            model_name='storyobject',
            name='base_of_operations',
            field=models.ForeignKey(to='personas.Location', blank=True, related_name='active_in', null=True),
        ),
        migrations.AlterField(
            model_name='storyobject',
            name='c_type',
            field=models.CharField(help_text='Select a story object category.', verbose_name='Story Object Type', max_length=32, choices=[('Protagonist', 'Protagonist'), ('Antagonist', 'Antagonist'), ('Supporting', 'Supporting'), ('Character', 'Character'), ('Creature', 'Creature'), ('Construct', 'Construct'), ('Thing', 'Thing'), ('Abstract', 'Abstract')], default='Character'),
        ),
    ]
