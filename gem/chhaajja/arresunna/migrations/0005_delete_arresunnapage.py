# Generated by Django 2.2.1 on 2019-05-11 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('arresunna', '0004_arresunnaindexpage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ArresunnaPage',
        ),
    ]
