# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0046_auto_20151008_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='description',
            field=django_markdown.models.MarkdownField(blank=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='content',
            field=django_markdown.models.MarkdownField(default='Enter your equipment here.', blank=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='content',
            field=django_markdown.models.MarkdownField(blank=True),
        ),
        migrations.AlterField(
            model_name='scene',
            name='description',
            field=django_markdown.models.MarkdownField(blank=True),
        ),
        migrations.AlterField(
            model_name='scratchpad',
            name='content',
            field=django_markdown.models.MarkdownField(blank=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='description',
            field=django_markdown.models.MarkdownField(blank=True),
        ),
    ]
