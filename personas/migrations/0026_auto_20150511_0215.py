# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0025_auto_20150510_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='relationship_class',
            field=models.CharField(max_length=32, choices=[('Ally', 'Ally'), ('Enemy', 'Enemy'), ('Friend', 'Friend'), ('Spouse', 'Spouse'), ('Parent', 'Parent'), ('Child', 'Child'), ('Sibling', 'Sibling'), ('Rival', 'Rival'), ('Lover', 'Lover'), ('Partner', 'Business Partner'), ('Member', 'Co-member'), ('Owner', 'Owner'), ('Likes', 'Likes'), ('Loves', 'Loves'), ('Hates', 'Hates'), ('Fears', 'Fears'), ('Envies', 'Envies'), ('Distrusts', 'Distrusts'), ('Trusts', 'Trusts'), ('Desires', 'Desires'), ('Respects', 'Respects'), ('Dislikes', 'Dislikes'), ('Is disgusted by', 'Is disgusted by'), ('Is angry at', 'Is angry at'), ('Is jealous of', 'Is jealous of'), ('Resents', 'Resents'), ('Is proud of', 'Is proud of'), ('Worships', 'Worships'), ('Reveres', 'Reveres'), ('Rules', 'Rules'), ('Leads', 'Leads'), ('Owns', 'Owns'), ('Belongs to', 'Belongs to'), ('Crews', 'Crews')], verbose_name='Defining Emotion', default='Ally'),
        ),
        migrations.AlterField(
            model_name='storyobject',
            name='c_type',
            field=models.CharField(help_text='Select a story object category.', max_length=32, choices=[('Character', 'Character'), ('Creature', 'Creature'), ('Thing', 'Thing'), ('Abstract', 'Abstract')], verbose_name='Story Object Type', default='Character'),
        ),
    ]
