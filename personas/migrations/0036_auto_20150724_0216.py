# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0035_auto_20150723_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='object_count',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='nation',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
