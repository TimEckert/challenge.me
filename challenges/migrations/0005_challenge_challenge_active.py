# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-22 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0004_auto_20180315_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='challenge_active',
            field=models.BooleanField(default=False),
        ),
    ]
