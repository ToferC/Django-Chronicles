# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personas', '0012_auto_20150427_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='creator',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='creator',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scene',
            name='creator',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='character',
            name='c_type',
            field=models.CharField(default='Supporting', max_length=32, choices=[('Protagonist', 'Protagonist'), ('Antagonist', 'Antagonist'), ('Supporting', 'Supporting'), ('Creature', 'Creature'), ('Construct', 'Construct'), ('Thing', 'Thing'), ('Abstract', 'Abstract')], verbose_name='Character Type'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scene',
            name='time',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='publication_date',
            field=models.DateField(auto_now=True),
            preserve_default=True,
        ),
    ]
