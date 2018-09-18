# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-05 15:21
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_GA_tracking_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sectionpage',
            name='featured_in_homepage_rotation',
        ),
        migrations.RemoveField(
            model_name='sitesettings',
            name='content_rotation',
        ),
        migrations.RemoveField(
            model_name='sitesettings',
            name='content_rotation_time',
        ),
        migrations.AddField(
            model_name='sectionpage',
            name='content_rotation_end_date',
            field=models.DateTimeField(blank=True, help_text=b'The date rotation will end', null=True),
        ),
        migrations.AddField(
            model_name='sectionpage',
            name='content_rotation_start_date',
            field=models.DateTimeField(blank=True, help_text=b'The date rotation will begin', null=True),
        ),
        migrations.AddField(
            model_name='sectionpage',
            name='friday_rotation',
            field=models.BooleanField(default=False, verbose_name=b'Friday'),
        ),
        migrations.AddField(
            model_name='sectionpage',
            name='monday_rotation',
            field=models.BooleanField(default=False, verbose_name=b'Monday'),
        ),
        migrations.AddField(
            model_name='sectionpage',
            name='saturday_rotation',
            field=models.BooleanField(default=False, verbose_name=b'Saturday'),
        ),
        migrations.AddField(
            model_name='sectionpage',
            name='sunday_rotation',
            field=models.BooleanField(default=False, verbose_name=b'Sunday'),
        ),
        migrations.AddField(
            model_name='sectionpage',
            name='thursday_rotation',
            field=models.BooleanField(default=False, verbose_name=b'Thursday'),
        ),
        migrations.AddField(
            model_name='sectionpage',
            name='time',
            field=wagtail.wagtailcore.fields.StreamField([(b'time', wagtail.wagtailcore.blocks.TimeBlock(required=False))], blank=True, help_text=b'The time/s content will be rotated', null=True),
        ),
        migrations.AddField(
            model_name='sectionpage',
            name='tuesday_rotation',
            field=models.BooleanField(default=False, verbose_name=b'Tuesday'),
        ),
        migrations.AddField(
            model_name='sectionpage',
            name='wednesday_rotation',
            field=models.BooleanField(default=False, verbose_name=b'Wednesday'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='content_rotation_end_date',
            field=models.DateTimeField(blank=True, help_text=b'The date rotation will end', null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='content_rotation_start_date',
            field=models.DateTimeField(blank=True, help_text=b'The date rotation will begin', null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='friday_rotation',
            field=models.BooleanField(default=False, verbose_name=b'Friday'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='monday_rotation',
            field=models.BooleanField(default=False, verbose_name=b'Monday'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='saturday_rotation',
            field=models.BooleanField(default=False, verbose_name=b'Saturday'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='sunday_rotation',
            field=models.BooleanField(default=False, verbose_name=b'Sunday'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='thursday_rotation',
            field=models.BooleanField(default=False, verbose_name=b'Thursday'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='time',
            field=wagtail.wagtailcore.fields.StreamField([(b'time', wagtail.wagtailcore.blocks.TimeBlock(required=False))], blank=True, help_text=b'The time/s content will be rotated', null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='tuesday_rotation',
            field=models.BooleanField(default=False, verbose_name=b'Tuesday'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='wednesday_rotation',
            field=models.BooleanField(default=False, verbose_name=b'Wednesday'),
        ),
        migrations.AlterField(
            model_name='sitelanguage',
            name='locale',
            field=models.CharField(choices=[(b'af', b'Afrikaans'), (b'ar', b'Arabic'), (b'ast', b'Asturian'), (b'az', b'Azerbaijani'), (b'bg', b'Bulgarian'), (b'be', b'Belarusian'), (b'bn', b'Bengali'), (b'br', b'Breton'), (b'bs', b'Bosnian'), (b'ca', b'Catalan'), (b'cs', b'Czech'), (b'cy', b'Welsh'), (b'da', b'Danish'), (b'de', b'German'), (b'el', b'Greek'), (b'en', b'English'), (b'en-au', b'Australian English'), (b'en-gb', b'British English'), (b'eo', b'Esperanto'), (b'es', b'Spanish'), (b'es-ar', b'Argentinian Spanish'), (b'es-co', b'Colombian Spanish'), (b'es-mx', b'Mexican Spanish'), (b'es-ni', b'Nicaraguan Spanish'), (b'es-ve', b'Venezuelan Spanish'), (b'et', b'Estonian'), (b'eu', b'Basque'), (b'fa', b'Persian'), (b'fi', b'Finnish'), (b'fr', b'French'), (b'fy', b'Frisian'), (b'ga', b'Irish'), (b'gd', b'Scottish Gaelic'), (b'gl', b'Galician'), (b'he', b'Hebrew'), (b'hi', b'Hindi'), (b'hr', b'Croatian'), (b'hu', b'Hungarian'), (b'ia', b'Interlingua'), (b'id', b'Indonesian'), (b'io', b'Ido'), (b'is', b'Icelandic'), (b'it', b'Italian'), (b'ja', b'Japanese'), (b'ka', b'Georgian'), (b'kk', b'Kazakh'), (b'km', b'Khmer'), (b'kn', b'Kannada'), (b'ko', b'Korean'), (b'lb', b'Luxembourgish'), (b'lt', b'Lithuanian'), (b'lv', b'Latvian'), (b'mk', b'Macedonian'), (b'ml', b'Malayalam'), (b'mn', b'Mongolian'), (b'mr', b'Marathi'), (b'my', b'Burmese'), (b'nb', b'Norwegian Bokmal'), (b'ne', b'Nepali'), (b'nl', b'Dutch'), (b'nn', b'Norwegian Nynorsk'), (b'os', b'Ossetic'), (b'pa', b'Punjabi'), (b'pl', b'Polish'), (b'pt', b'Portuguese'), (b'pt-br', b'Brazilian Portuguese'), (b'ro', b'Romanian'), (b'ru', b'Russian'), (b'sk', b'Slovak'), (b'sl', b'Slovenian'), (b'sq', b'Albanian'), (b'sr', b'Serbian'), (b'sr-latn', b'Serbian Latin'), (b'sv', b'Swedish'), (b'sw', b'Swahili'), (b'ta', b'Tamil'), (b'te', b'Telugu'), (b'th', b'Thai'), (b'tr', b'Turkish'), (b'tt', b'Tatar'), (b'udm', b'Udmurt'), (b'uk', b'Ukrainian'), (b'ur', b'Urdu'), (b'vi', b'Vietnamese'), (b'zh-hans', b'Simplified Chinese'), (b'zh-hant', b'Traditional Chinese'), (b'zu', 'Zulu'), (b'xh', 'Xhosa'), (b'st', 'Sotho'), (b've', 'Venda'), (b'tn', 'Tswana'), (b'ts', 'Tsonga'), (b'ss', 'Swati'), (b'nr', 'Ndebele')], help_text='Site language', max_length=255, verbose_name='language name'),
        ),
    ]