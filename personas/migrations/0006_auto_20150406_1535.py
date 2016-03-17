# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personas', '0005_note_nation'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('image', models.ImageField(default='content_images/nothing.jpg', upload_to='content_images/%Y/%m/%d')),
                ('title', models.CharField(max_length=32)),
                ('date', models.DateTimeField(auto_now=True)),
                ('rating', models.PositiveSmallIntegerField(default=0)),
                ('chapter', models.ForeignKey(null=True, to='personas.Chapter', blank=True)),
                ('character', models.ForeignKey(null=True, to='personas.Character', blank=True)),
                ('creator', models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(null=True, to='personas.Item', blank=True)),
                ('location', models.ForeignKey(null=True, to='personas.Location', blank=True)),
                ('nation', models.ForeignKey(null=True, to='personas.Nation', blank=True)),
                ('organization', models.ForeignKey(null=True, to='personas.Organization', blank=True)),
                ('scene', models.ForeignKey(null=True, to='personas.Scene', blank=True)),
                ('story', models.ForeignKey(null=True, to='personas.Story', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='story',
            name='colour_theme',
            field=models.CharField(default='Dark', choices=[('Light', 'Light'), ('Dark', 'Dark')], max_length=12),
            preserve_default=True,
        ),
    ]
