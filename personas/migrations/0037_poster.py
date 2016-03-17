# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personas', '0036_auto_20150724_0216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', django_markdown.models.MarkdownField(blank=True)),
                ('publication_date', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
