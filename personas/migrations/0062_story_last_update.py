# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0061_storyobject_core_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='last_update',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
