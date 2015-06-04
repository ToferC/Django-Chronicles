# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0031_auto_20150530_0522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='story',
        ),
        migrations.RemoveField(
            model_name='item',
            name='storyobject',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='storyobject',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='location',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='members',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='story',
        ),
        migrations.RemoveField(
            model_name='ability',
            name='item',
        ),
        migrations.RemoveField(
            model_name='galleryimage',
            name='item',
        ),
        migrations.RemoveField(
            model_name='galleryimage',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='note',
            name='item',
        ),
        migrations.RemoveField(
            model_name='note',
            name='organization',
        ),
        migrations.AddField(
            model_name='chapter',
            name='published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='location',
            name='published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='nation',
            name='published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='scene',
            name='published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='story',
            name='published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='storyobject',
            name='published',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='mainmap',
            name='tiles',
            field=models.CharField(blank=True, default='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', max_length=256),
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Membership',
        ),
        migrations.DeleteModel(
            name='Organization',
        ),
    ]
