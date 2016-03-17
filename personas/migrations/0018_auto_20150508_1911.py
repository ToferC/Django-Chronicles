# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0017_auto_20150508_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='from_storyobject',
            field=models.ForeignKey(to='personas.StoryObject', related_name='from_storyobject'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='to_storyobject',
            field=models.ForeignKey(to='personas.StoryObject', related_name='to_storyobject'),
        ),
        migrations.AlterField(
            model_name='storyobject',
            name='c_type',
            field=models.CharField(choices=[('Protagonist', 'Protagonist'), ('Antagonist', 'Antagonist'), ('Supporting', 'Supporting'), ('Character', 'Character'), ('Creature', 'Creature'), ('Construct', 'Construct'), ('Thing', 'Thing'), ('Abstract', 'Abstract')], max_length=32, verbose_name='Story Object Type', default='Character'),
        ),
    ]
