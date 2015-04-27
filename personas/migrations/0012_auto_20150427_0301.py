# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0011_auto_20150423_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='c_type',
            field=models.CharField(max_length=32, verbose_name='Character Type', default='Supporting', choices=[('Protagonist', 'Protagonist'), ('Antagonist', 'Antagonist'), ('Supporting', 'Supporting'), ('Creature', 'Creature'), ('Construct', 'Construct')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='note',
            name='content',
            field=django_markdown.models.MarkdownField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='relationship',
            name='relationship_class',
            field=models.CharField(max_length=32, default='Ally', choices=[('Ally', 'Ally'), ('Enemy', 'Enemy'), ('Friend', 'Friend'), ('Spouse', 'Spouse'), ('Parent', 'Parent'), ('Child', 'Child'), ('Sibling', 'Sibling'), ('Rival', 'Rival'), ('Lover', 'Lover'), ('Partner', 'Business Partner'), ('Member', 'Co-member'), ('Owner', 'Owner')]),
            preserve_default=True,
        ),
    ]
