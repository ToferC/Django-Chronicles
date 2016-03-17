# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0014_auto_20150501_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scene',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True),
            preserve_default=True,
        ),
    ]
