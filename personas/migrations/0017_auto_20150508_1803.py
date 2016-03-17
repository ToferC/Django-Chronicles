# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personas', '0016_scene_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Character',
            new_name='StoryObject',
            ),
        migrations.RenameField(
            model_name='combatinfo',
            old_name='character',
            new_name='storyobject'
            ),
        migrations.RenameField(
            model_name='galleryimage',
            old_name='character',
            new_name='storyobject'
            ),
        migrations.RenameField(
            model_name='item',
            old_name='character',
            new_name='storyobject'
            ),
        migrations.RenameField(
            model_name='membership',
            old_name='character',
            new_name='storyobject'
            ),
        migrations.RenameField(
            model_name='note',
            old_name='character',
            new_name='storyobject'
            ),
        migrations.RenameField(
            model_name='relationship',
            old_name='from_character',
            new_name='from_storyobject'
            ),
        migrations.RenameField(
            model_name='relationship',
            old_name='to_character',
            new_name='to_storyobject'
            ),
        migrations.RenameField(
            model_name='scene',
            old_name='characters',
            new_name='storyobjects'
            ),
        migrations.RenameField(
            model_name='scratchpad',
            old_name='character',
            new_name='storyobject'
            ),
        migrations.RenameField(
            model_name='skill',
            old_name='character',
            new_name='storyobject'
            ),
        migrations.RenameField(
            model_name='specialability',
            old_name='character',
            new_name='storyobject'
            ),
        migrations.RenameField(
            model_name='statistic',
            old_name='character',
            new_name='storyobject'
            ),
        migrations.RenameField(
            model_name='trait',
            old_name='character',
            new_name='storyobject'
            ),
        migrations.AlterField(
            model_name='communique',
            name='author',
            field=models.ForeignKey(to='personas.StoryObject', related_name='Author'),
        ),
        migrations.AlterField(
            model_name='communique',
            name='receiver',
            field=models.ForeignKey(to='personas.StoryObject', related_name='Receiver'),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='organization',
            name='members',
            field=models.ManyToManyField(blank=True, through='personas.Membership', to='personas.StoryObject'),
        ),
    ]
