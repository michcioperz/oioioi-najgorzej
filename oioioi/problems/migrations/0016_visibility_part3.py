# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-06-15 18:43
# ADJUSTED manually, see part1 file
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0015_visibility_part2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='is_public',
        ),
    ]
