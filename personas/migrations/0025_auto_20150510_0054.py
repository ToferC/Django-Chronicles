# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0024_auto_20150510_0048'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SpecialAbility',
            new_name='Ability',
        ),
    ]
