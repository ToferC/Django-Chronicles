# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0020_auto_20150508_1944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scene',
            old_name='time',
            new_name='publication_date',
        ),
        migrations.AddField(
            model_name='scene',
            name='purpose',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AddField(
            model_name='scene',
            name='resolution',
            field=models.CharField(default='Neutral', choices=[('Up', 'Up'), ('Down', 'Down'), ('Neutral', 'Neutral')], max_length=8),
        ),
        migrations.AddField(
            model_name='scene',
            name='scene_type',
            field=models.CharField(default='Dramatic', choices=[('Dramatic', 'Dramatic'), ('Action', 'Action'), ('Suspense', 'Suspense'), ('Question', 'Question'), ('Reveal', 'Reveal'), ('Prodecural', 'Procedural')], max_length=32),
        ),
        migrations.AlterField(
            model_name='storyobject',
            name='nationality',
            field=models.ForeignKey(blank=True, null=True, to='personas.Nation'),
        ),
    ]
