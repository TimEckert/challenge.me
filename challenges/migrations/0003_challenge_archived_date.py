# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-15 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0002_challenge_teaser'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='archived_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
