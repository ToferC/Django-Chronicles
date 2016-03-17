# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0052_auto_20160127_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='zoom',
            field=models.IntegerField(help_text='Sets the default zoom for your place', default=6),
        ),
    ]
