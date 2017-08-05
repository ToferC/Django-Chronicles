# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0060_auto_20161221_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='storyobject',
            name='core_role',
            field=models.BooleanField(default=False, help_text='Select if this is a player character, a major protagonist \n        or otherwise a critical element to your story. These elements will show up first\n        in lists and have a graphic distinction.\n        '),
        ),
    ]
