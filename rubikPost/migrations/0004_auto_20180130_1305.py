# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-30 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rubikPost', '0003_auto_20180126_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='Slug will be generated automatically.', unique=True),
        ),
    ]
