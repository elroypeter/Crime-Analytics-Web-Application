# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-18 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180518_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crimes_against_women',
            name='Year',
            field=models.CharField(max_length=140),
        ),
    ]