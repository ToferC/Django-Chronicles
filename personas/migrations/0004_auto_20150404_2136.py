# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0003_auto_20150403_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='nation',
            name='image',
            field=models.ImageField(default='nation_images/nothing.jpg', upload_to='nation_images/%Y/%m/%d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='combatinfo',
            name='data',
            field=models.CharField(default=0, max_length=128),
            preserve_default=True,
        ),
    ]
