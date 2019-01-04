# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-02 07:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_app_package_seq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=64, unique=True)),
                ('committer', models.CharField(default='admin', max_length=32)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('failed', 'failed'), ('success', 'success')], default='success', max_length=16)),
                ('branch', models.CharField(max_length=16)),
                ('sort_id', models.CharField(max_length=16)),
                ('env', models.CharField(max_length=16)),
                ('package_path', models.CharField(max_length=256)),
                ('log_path', models.CharField(max_length=256)),
                ('app_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.App')),
            ],
        ),
    ]