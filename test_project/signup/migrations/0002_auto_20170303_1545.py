# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='civilite',
            field=models.BooleanField(default=False),
        ),
    ]
