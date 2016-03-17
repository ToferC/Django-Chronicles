# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='skill_type_name_1',
            field=models.CharField(default='General', max_length=24),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='skill_type_name_2',
            field=models.CharField(default='Investigative', max_length=24),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='skill_type_name_3',
            field=models.CharField(default='Combat', max_length=24),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='skill_type_name_4',
            field=models.CharField(default='Knowledge', max_length=24),
            preserve_default=True,
        ),
    ]
