# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0028_auto_20150511_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='relationship_class',
            field=models.CharField(verbose_name='Defining Emotion', max_length=32, default='Ally'),
        ),
        migrations.AlterField(
            model_name='storyobject',
            name='image',
            field=models.ImageField(upload_to='profile_images/%Y/%m/%d/%H/%M/%S', default='profile_images/shadow_figure.jpeg'),
        ),
    ]
