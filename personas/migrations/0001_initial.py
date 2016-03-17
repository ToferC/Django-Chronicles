# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True)),
                ('number', models.PositiveSmallIntegerField(verbose_name='Chapter Number', default=1)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('c_type', models.CharField(default='Supporting', verbose_name='Character Type', choices=[('Protagonist', 'Protagonist'), ('Antagonist', 'Antagonist'), ('Supporting', 'Supporting'), ('Creature', 'Creature')], max_length=32)),
                ('xp', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('description', models.TextField(blank=True)),
                ('age', models.PositiveSmallIntegerField(default=21)),
                ('combat_info', django_markdown.models.MarkdownField(default='Attack: X, Defense: X')),
                ('image', models.ImageField(default='profile_images/nobody.jpg', upload_to='profile_images/%Y/%m/%d')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CombatInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('data', models.CharField(default=0, max_length=64)),
                ('character', models.ForeignKey(to='personas.Character')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Communique',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=140)),
                ('rating', models.PositiveSmallIntegerField(default=0)),
                ('author', models.ForeignKey(to='personas.Character', related_name='Author')),
                ('receiver', models.ForeignKey(to='personas.Character', related_name='Receiver')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('character', models.ForeignKey(to='personas.Character', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('image', models.ImageField(default='location_images/nowhere.jpg', upload_to='location_images/%Y/%m/%d')),
                ('terrain', models.CharField(max_length=128)),
                ('features', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True)),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
                ('slug', models.SlugField(unique=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MainMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('base_latitude', models.FloatField(blank=True)),
                ('base_longitude', models.FloatField(blank=True)),
                ('tiles', models.CharField(blank=True, max_length=256)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date_joined', models.DateField(default='2014-01-01')),
                ('role', models.CharField(max_length=128)),
                ('rank', models.PositiveSmallIntegerField(default=1)),
                ('character', models.ForeignKey(to='personas.Character')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True)),
                ('might', models.PositiveSmallIntegerField(default=0)),
                ('intrigue', models.PositiveSmallIntegerField(default=0)),
                ('magic', models.PositiveSmallIntegerField(default=0)),
                ('wealth', models.PositiveSmallIntegerField(default=0)),
                ('influence', models.PositiveSmallIntegerField(default=0)),
                ('defense', models.PositiveSmallIntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('rating', models.PositiveSmallIntegerField(default=0)),
                ('chapter', models.ForeignKey(to='personas.Chapter', blank=True, null=True)),
                ('character', models.ForeignKey(to='personas.Character', blank=True, null=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, default=0)),
                ('item', models.ForeignKey(to='personas.Item', blank=True, null=True)),
                ('location', models.ForeignKey(to='personas.Location', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True)),
                ('purpose', models.CharField(max_length=128)),
                ('region', models.CharField(max_length=128)),
                ('slug', models.SlugField(unique=True)),
                ('location', models.ForeignKey(to='personas.Location')),
                ('members', models.ManyToManyField(blank=True, to='personas.Character', through='personas.Membership')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('relationship_class', models.CharField(default='Ally', choices=[('Ally', 'Ally'), ('Enemy', 'Enemy'), ('Friend', 'Friend'), ('Spouse', 'Spouse'), ('Parent', 'Parent'), ('Child', 'Child'), ('Sibling', 'Sibling'), ('Rival', 'Rival'), ('Lover', 'Lover'), ('Partner', 'Business Partner'), ('Member', 'Co-member')], max_length=32)),
                ('weight', models.PositiveSmallIntegerField(verbose_name='Strength of the relationship %', default=50)),
                ('relationship_description', models.CharField(max_length=128)),
                ('from_character', models.ForeignKey(to='personas.Character', related_name='from_character')),
                ('to_character', models.ForeignKey(to='personas.Character', related_name='to_character')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True)),
                ('time', models.DateTimeField(default='2014-01-01')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('chapter', models.ForeignKey(to='personas.Chapter')),
                ('characters', models.ManyToManyField(blank=True, to='personas.Character')),
                ('location', models.ForeignKey(blank=True, to='personas.Location')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('value', models.PositiveSmallIntegerField(default=0)),
                ('s_type', models.CharField(default='Type_1', verbose_name='Skill Type', choices=[('Type_1', 'Type_1'), ('Type_2', 'Type_2'), ('Type_3', 'Type_3'), ('Type_4', 'Type_4')], max_length=32)),
                ('description', models.TextField(blank=True)),
                ('character', models.ForeignKey(to='personas.Character')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpecialAbility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField(blank=True)),
                ('character', models.ForeignKey(to='personas.Character', blank=True, null=True)),
                ('item', models.ForeignKey(to='personas.Item', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('value', models.PositiveSmallIntegerField(default=0)),
                ('stat_type', models.CharField(default='Type_1', verbose_name='Statistic Type', choices=[('Type_1', 'Type_1'), ('Type_2', 'Type_2'), ('Type_3', 'Type_3'), ('Type_4', 'Type_4')], max_length=32)),
                ('description', models.TextField(blank=True)),
                ('character', models.ForeignKey(to='personas.Character')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('publication_date', models.DateField()),
                ('description', models.TextField(blank=True)),
                ('genre', models.CharField(default='Fantasy', choices=[('Supers', 'Supers'), ('Fantasy', 'Fantasy'), ('Horror', 'Horror'), ('Historical', 'Historical'), ('Science-Fiction', 'Science Fiction'), ('Western', 'Western'), ('Drama', 'Drama'), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Fable', 'Fable'), ('Mystery', 'Mystery')], max_length=128)),
                ('image', models.ImageField(default='story_images/nobody.jpg', upload_to='story_images/%Y/%m/%d')),
                ('background', models.ImageField(default='story_backgrounds/nothing.jpg', upload_to='story_backgrounds/%Y/%m/%d')),
                ('slug', models.SlugField(unique=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('label', models.CharField(blank=True, default='CO', choices=[('CO', 'Core'), ('VA', 'Values'), ('BA', 'Background'), ('FL', 'Flaw')], max_length=12)),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('character', models.ForeignKey(to='personas.Character')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('website', models.URLField(blank=True)),
                ('image', models.ImageField(default='user_images/nobody.jpg', upload_to='user_images/%Y/%m/%d')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='organization',
            name='story',
            field=models.ForeignKey(to='personas.Story'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='note',
            name='organization',
            field=models.ForeignKey(to='personas.Organization', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='note',
            name='scene',
            field=models.ForeignKey(to='personas.Scene', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='note',
            name='story',
            field=models.ForeignKey(to='personas.Story', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nation',
            name='story',
            field=models.ForeignKey(to='personas.Story'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membership',
            name='organization',
            field=models.ForeignKey(to='personas.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mainmap',
            name='story',
            field=models.ForeignKey(to='personas.Story'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='nation',
            field=models.ForeignKey(blank=True, to='personas.Nation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='story',
            field=models.ForeignKey(to='personas.Story', default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='story',
            field=models.ForeignKey(to='personas.Story', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='base_of_operations',
            field=models.ForeignKey(to='personas.Location', related_name='active_in', default=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='birthplace',
            field=models.ForeignKey(to='personas.Location', related_name='place_of_birth', default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='creator',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='nationality',
            field=models.ForeignKey(to='personas.Nation', default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='story',
            field=models.ForeignKey(to='personas.Story', default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chapter',
            name='story',
            field=models.ForeignKey(to='personas.Story'),
            preserve_default=True,
        ),
    ]
