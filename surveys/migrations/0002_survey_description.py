# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
