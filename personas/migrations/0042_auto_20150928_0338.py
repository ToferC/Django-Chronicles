# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0041_auto_20150919_0104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryimage',
            name='location',
        ),
        migrations.RemoveField(
            model_name='note',
            name='location',
        ),
        migrations.RemoveField(
            model_name='scene',
            name='location',
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='place',
            field=models.ForeignKey(to='personas.Place', blank=True, null=True, related_name='loc2image'),
        ),
        migrations.AddField(
            model_name='note',
            name='place',
            field=models.ForeignKey(to='personas.Place', blank=True, null=True, related_name='loc2note'),
        ),
        migrations.AddField(
            model_name='scene',
            name='place',
            field=models.ForeignKey(to='personas.Place', blank=True, null=True, related_name='loc2scene'),
            preserve_default=False,
        ),
    ]
