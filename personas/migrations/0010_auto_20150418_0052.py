# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0009_story_map_tile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trait',
            name='slug',
        ),
        migrations.AddField(
            model_name='character',
            name='scratchpad',
            field=django_markdown.models.MarkdownField(blank=True),
            preserve_default=True,
        ),
    ]
