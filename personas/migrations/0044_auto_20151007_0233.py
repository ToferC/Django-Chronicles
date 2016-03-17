# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0043_auto_20151004_0105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='location',
            name='nation',
        ),
        migrations.RemoveField(
            model_name='location',
            name='story',
        ),
        migrations.RemoveField(
            model_name='nation',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='nation',
            name='story',
        ),
        migrations.RemoveField(
            model_name='galleryimage',
            name='nation',
        ),
        migrations.RemoveField(
            model_name='note',
            name='nation',
        ),
        migrations.RemoveField(
            model_name='storyobject',
            name='base_of_operations',
        ),
        migrations.RemoveField(
            model_name='storyobject',
            name='nationality',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Nation',
        ),
    ]
