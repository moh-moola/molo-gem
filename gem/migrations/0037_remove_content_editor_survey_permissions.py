# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-10 10:15
from __future__ import unicode_literals

from django.db import migrations
from django.core.management.sql import emit_post_migrate_signal


def get_group(Group, group_name):
    group, _created = Group.objects.get_or_create(name=group_name)
    return group


def remove_page_permission(GroupPagePermission, group, pages, page_permission_type):
    for page in pages.iterator():
        for permission_type in page_permission_type:
            permission = GroupPagePermission.objects.get(
                group=group, page=page, permission_type=permission_type
            )
            permission.delete()


def remove_content_editor_survey_permissions(apps, schema_editor):
    db_alias = schema_editor.connection.alias

    emit_post_migrate_signal(2, False, db_alias)
    Group = apps.get_model('auth.Group')
    content_editor_group = get_group(Group, 'content_editor')
    SurveysIndexPage = apps.get_model('surveys.SurveysIndexPage')

    # Wagtail Page permission
    GroupPagePermission = apps.get_model('wagtailcore.GroupPagePermission')
    page_permission_types = ('add', 'edit', 'publish', 'bulk_delete', 'lock')

    surveys = SurveysIndexPage.objects.all()
    remove_page_permission(GroupPagePermission, content_editor_group, surveys, page_permission_types)


class Migration(migrations.Migration):

    dependencies = [
        ('gem', '0036_gemsettings_fb_enable_chat_bot'),
    ]

    operations = [
        # migrations.RunPython(remove_content_editor_survey_permissions),
    ]
