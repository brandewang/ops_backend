# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-01 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_app_packing_lock'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='package_seq',
            field=models.IntegerField(default=0),
        ),
    ]
