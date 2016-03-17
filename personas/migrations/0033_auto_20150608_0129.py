# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personas', '0032_auto_20150604_0236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('content', models.TextField(default='Enter your equipment here.')),
                ('date', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, default=0)),
            ],
        ),
        migrations.AddField(
            model_name='storyobject',
            name='equipment_toggle',
            field=models.BooleanField(verbose_name='Enable Equipment?', default=True, help_text='Check to enable equipment for this story object.'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='published',
            field=models.BooleanField(default=True, help_text='Elements that are NOT published will only be viewable in your Workshop.'),
        ),
        migrations.AlterField(
            model_name='location',
            name='image',
            field=models.ImageField(default='profile_images/shadow_figure.jpeg', upload_to='location_images/%Y/%m/%d/%H_%M_%S'),
        ),
        migrations.AlterField(
            model_name='location',
            name='published',
            field=models.BooleanField(default=True, help_text='Elements that are NOT published will only be viewable in your Workshop.'),
        ),
        migrations.AlterField(
            model_name='nation',
            name='image',
            field=models.ImageField(default='profile_images/shadow_figure.jpeg', upload_to='nation_images/%Y/%m/%d/%H_%M_%S'),
        ),
        migrations.AlterField(
            model_name='nation',
            name='published',
            field=models.BooleanField(default=True, help_text='Elements that are NOT published will only be viewable in your Workshop.'),
        ),
        migrations.AlterField(
            model_name='scene',
            name='published',
            field=models.BooleanField(default=True, help_text='Elements that are NOT published will only be viewable in your Workshop.'),
        ),
        migrations.AlterField(
            model_name='story',
            name='background',
            field=models.ImageField(default='profile_images/shadow_figure.jpeg', upload_to='story_backgrounds/%Y/%m/%d/%H_%M_%S'),
        ),
        migrations.AlterField(
            model_name='story',
            name='image',
            field=models.ImageField(default='profile_images/shadow_figure.jpeg', upload_to='story_images/%Y/%m/%d/%H_%M_%S'),
        ),
        migrations.AlterField(
            model_name='story',
            name='published',
            field=models.BooleanField(default=True, help_text='Elements that are NOT published will only be viewable in your Workshop.'),
        ),
        migrations.AlterField(
            model_name='storyobject',
            name='c_type',
            field=models.CharField(max_length=32, choices=[('Force', 'Force'), ('Character', 'Character'), ('Creature', 'Creature'), ('Organization', 'Organization'), ('Thing', 'Thing')], default='Character', verbose_name='Story Object Type', help_text='Select a story object category.'),
        ),
        migrations.AlterField(
            model_name='storyobject',
            name='published',
            field=models.BooleanField(default=True, help_text='Elements that are NOT published will only be viewable in your Workshop.'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='profile_images/shadow_figure.jpeg', upload_to='user_images/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='storyobject',
            field=models.ForeignKey(null=True, to='personas.StoryObject', blank=True),
        ),
    ]
