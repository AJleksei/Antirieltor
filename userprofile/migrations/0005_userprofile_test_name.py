# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_remove_userprofile_test_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='test_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
