# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-19 07:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gem', '0022_text_banner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentcountrule',
            name='segment',
        ),
        migrations.RemoveField(
            model_name='profiledatarule',
            name='segment',
        ),
        migrations.DeleteModel(
            name='CommentCountRule',
        ),
        migrations.DeleteModel(
            name='ProfileDataRule',
        ),
    ]
