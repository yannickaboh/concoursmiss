# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-13 17:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concours', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gprovince',
            name='libelle',
        ),
        migrations.RemoveField(
            model_name='gprovince',
            name='slogan',
        ),
    ]
