# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 22:19
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='album',
            field=models.CharField(default=b'*', max_length=50),
        ),
        migrations.AddField(
            model_name='track',
            name='track_rating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(default=b'R&B', max_length=50, unique=True),
        ),
    ]
