# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-07-11 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20220711_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='slug',
            field=models.SlugField(blank=True, editable=False),
        ),
    ]