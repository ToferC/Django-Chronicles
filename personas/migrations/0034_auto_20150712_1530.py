# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0033_auto_20150608_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ability',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='nation',
            name='might',
            field=models.PositiveSmallIntegerField(default=0, help_text='This field and the fields below can be used to set values for\n        the relative power of different areas or regions in a game.'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='weight',
            field=models.CharField(max_length=64, default='5', verbose_name='Numerical Rating', help_text='If your story uses it, enter a numerical rating for the relationship here.'),
        ),
        migrations.AlterField(
            model_name='story',
            name='skill_type_name_1',
            field=models.CharField(max_length=24, default='General', blank=True, help_text='This field and the skill fields below set the name for different skill types in a game.\n        They are optional.'),
        ),
        migrations.AlterField(
            model_name='story',
            name='statistic_type_name_1',
            field=models.CharField(max_length=24, default='Physical', blank=True, help_text='This field and the statistic fields below set the name for different stat types in a game.\n        They are optional.'),
        ),
    ]
