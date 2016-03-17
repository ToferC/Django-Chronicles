# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0007_auto_20150407_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='image',
            field=models.ImageField(default='organization_images/nothing.jpg', upload_to='organization_images/%Y/%m/%d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='skill_type_name_1',
            field=models.CharField(default='General', max_length=24, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='skill_type_name_2',
            field=models.CharField(default='Investigative', max_length=24, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='skill_type_name_3',
            field=models.CharField(default='Combat', max_length=24, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='skill_type_name_4',
            field=models.CharField(default='Knowledge', max_length=24, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='statistic_type_name_1',
            field=models.CharField(default='Physical', max_length=24, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='statistic_type_name_2',
            field=models.CharField(default='Mental', max_length=24, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='statistic_type_name_3',
            field=models.CharField(default='Social', max_length=24, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='statistic_type_name_4',
            field=models.CharField(default='Magic', max_length=24, blank=True),
            preserve_default=True,
        ),
    ]
