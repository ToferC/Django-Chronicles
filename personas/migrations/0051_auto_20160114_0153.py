# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0050_auto_20160112_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='other_notifications',
            field=models.BooleanField(default=True, help_text='Enable this to get email notifications for changes other people make.'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='own_notifications',
            field=models.BooleanField(default=False, help_text='Enable this to get email notifications for your own changes.'),
        ),
    ]
