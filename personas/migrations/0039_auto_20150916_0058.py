# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0038_auto_20150912_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('storyobject_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, to='personas.StoryObject', serialize=False)),
                ('latitude', models.FloatField(default=50.0)),
                ('longitude', models.FloatField(default=-1.0)),
            ],
            bases=('personas.storyobject',),
        ),
        migrations.AlterField(
            model_name='storyobject',
            name='c_type',
            field=models.CharField(verbose_name='Story Object Type', default='Character', choices=[('Force', 'Force'), ('Character', 'Character'), ('Creature', 'Creature'), ('Organization', 'Organization'), ('Place', 'Place'), ('Thing', 'Thing')], max_length=32, help_text='Select a story object category.'),
        ),
    ]
