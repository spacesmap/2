# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 16:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0008_auto_20170915_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='place.Place'),
        ),
    ]
