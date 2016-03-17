# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0030_auto_20150519_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(default='content_images/nothing.jpg', upload_to='content_images/%Y/%m/%d/%H_%M_%S'),
        ),
        migrations.AlterField(
            model_name='location',
            name='image',
            field=models.ImageField(default='location_images/nowhere.jpg', upload_to='location_images/%Y/%m/%d/%H_%M_%S'),
        ),
        migrations.AlterField(
            model_name='nation',
            name='image',
            field=models.ImageField(default='nation_images/nothing.jpg', upload_to='nation_images/%Y/%m/%d/%H_%M_%S'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='image',
            field=models.ImageField(default='organization_images/nothing.jpg', upload_to='organization_images/%Y/%m/%d/%H_%M_%S'),
        ),
        migrations.AlterField(
            model_name='story',
            name='background',
            field=models.ImageField(default='story_backgrounds/nothing.jpg', upload_to='story_backgrounds/%Y/%m/%d/%H_%M_%S'),
        ),
        migrations.AlterField(
            model_name='story',
            name='image',
            field=models.ImageField(default='story_images/nobody.jpg', upload_to='story_images/%Y/%m/%d/%H_%M_%S'),
        ),
        migrations.AlterField(
            model_name='storyobject',
            name='image',
            field=models.ImageField(default='profile_images/shadow_figure.jpeg', upload_to='profile_images/%Y/%m/%d/%H_%M_%S'),
        ),
    ]
