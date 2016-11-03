# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-02 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_bannerpage_external_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='enable_clickable_tags',
            field=models.BooleanField(default=False, verbose_name=b'Display tags on Front-end'),
        ),
    ]
