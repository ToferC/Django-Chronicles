# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personas', '0010_auto_20150418_0052'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScratchPad',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('content', django_markdown.models.MarkdownField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('character', models.ForeignKey(null=True, blank=True, to='personas.Character')),
                ('creator', models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='character',
            name='scratchpad',
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='title',
            field=models.CharField(max_length=64),
            preserve_default=True,
        ),
    ]
