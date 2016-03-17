# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0023_auto_20150510_0011'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Trait',
            new_name='Aspect',
        ),
        migrations.AlterField(
            model_name='relationship',
            name='relationship_class',
            field=models.CharField(verbose_name='Defining Emotion', max_length=32, choices=[('Ally', 'Ally'), ('Enemy', 'Enemy'), ('Friend', 'Friend'), ('Spouse', 'Spouse'), ('Parent', 'Parent'), ('Child', 'Child'), ('Sibling', 'Sibling'), ('Rival', 'Rival'), ('Lover', 'Lover'), ('Partner', 'Business Partner'), ('Member', 'Co-member'), ('Owner', 'Owner'), ('Loves', 'Loves'), ('Hates', 'Hates'), ('Fears', 'Fears'), ('Envies', 'Envies'), ('Distrusts', 'Distrusts'), ('Trusts', 'Trusts'), ('Desires', 'Desires'), ('Respects', 'Respects'), ('Dislikes', 'Dislikes'), ('Is disgusted by', 'Is disgusted by'), ('Is angry at', 'Is angry at'), ('Is jealous of', 'Is jealous of'), ('Resents', 'Resents'), ('Is proud of', 'Is proud of'), ('Worships', 'Worships'), ('Reveres', 'Reveres'), ('Rules', 'Rules'), ('Leads', 'Leads'), ('Owns', 'Owns'), ('Belongs to', 'Belongs to'), ('Crews', 'Crews')], default='Ally'),
        ),
    ]
