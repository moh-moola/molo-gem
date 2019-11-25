# Generated by Django 2.2.7 on 2019-11-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gem', '0039_gemsettings_enable_comment_threads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gemsettings',
            name='enable_comment_threads',
            field=models.BooleanField(default=False, help_text='When enabled user comments will be shown on the front-end.'),
        ),
    ]
