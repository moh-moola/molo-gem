from datetime import datetime, timedelta
from json import dumps
import pytest
from django.test import TestCase


from molo.core.models import SiteLanguage, FooterPage
from molo.core.tests.base import MoloTestCaseMixin

from molo.core.tasks import rotate_content

from wagtail.wagtailcore.models import Site
from wagtail.contrib.settings.context_processors import SettingsProxy


@pytest.mark.django_db
class TestTasks(TestCase, MoloTestCaseMixin):

    def setUp(self):
        # Creates Main language
        self.english = SiteLanguage.objects.create(
            locale='en',
        )
        self.mk_main()

        self.yourmind = self.mk_section(
            self.section_index, title='Your mind')
        self.yourmind_sub = self.mk_section(
            self.yourmind, title='Your mind subsection')

    def test_latest_rotation_on(self):
        site = Site.objects.get(is_default_site=True)
        settings = SettingsProxy(site)
        site_settings = settings['core']['SiteSettings']

        site_settings.content_rotation_start_date = datetime.now()
        site_settings.content_rotation_end_date = datetime.now() + timedelta(
            days=1)
        time1 = str(datetime.now().time())
        time2 = str((datetime.now() + timedelta(minutes=1)).time())
        site_settings.time = dumps([{
            'type': 'time', 'value': time1}, {'type': 'time', 'value': time2}])
        site_settings.m = True
        site_settings.tu = True
        site_settings.w = True
        site_settings.th = True
        site_settings.f = True
        site_settings.sa = True
        site_settings.su = True
        site_settings.save()

        for i in range(5):
            self.footer = FooterPage(
                title='Footer Page %s', slug='footer-page-%s' % (i, ))
            self.footer_index.add_child(instance=self.footer)

        self.assertEquals(FooterPage.objects.live().count(), 5)
        self.assertEquals(self.main.latest_articles().count(), 0)

        self.mk_articles(self.yourmind_sub, count=10, featured_in_latest=True)
        self.mk_articles(self.yourmind_sub, count=10, featured_in_latest=False)
        self.assertEquals(self.main.latest_articles().count(), 10)
        first_article_old = self.main.latest_articles()[0].pk
        last_article_old = self.main.latest_articles()[9].pk

        rotate_content()

        self.assertEquals(self.main.latest_articles().count(), 10)
        self.assertNotEquals(
            first_article_old, self.main.latest_articles()[0].pk)
        self.assertEquals(
            first_article_old, self.main.latest_articles()[2].pk)
        self.assertNotEquals(
            last_article_old, self.main.latest_articles()[8].pk)

    def test_latest_rotation_no_days(self):
        site = Site.objects.get(is_default_site=True)
        settings = SettingsProxy(site)
        site_settings = settings['core']['SiteSettings']

        site_settings.content_rotation_start_date = datetime.now()
        site_settings.content_rotation_end_date = datetime.now() + timedelta(
            days=1)
        time1 = str(datetime.now().time())
        time2 = str((datetime.now() + timedelta(minutes=1)).time())
        site_settings.time = dumps([{
            'type': 'time', 'value': time1}, {'type': 'time', 'value': time2}])
        site_settings.save()

        for i in range(5):
            self.footer = FooterPage(
                title='Footer Page %s', slug='footer-page-%s' % (i, ))
            self.footer_index.add_child(instance=self.footer)

        self.assertEquals(FooterPage.objects.live().count(), 5)
        self.assertEquals(self.main.latest_articles().count(), 0)

        self.mk_articles(self.yourmind_sub, count=10, featured_in_latest=True)
        self.mk_articles(self.yourmind_sub, count=10, featured_in_latest=False)
        self.assertEquals(self.main.latest_articles().count(), 10)
        first_article_old = self.main.latest_articles()[0].pk
        last_article_old = self.main.latest_articles()[9].pk
        rotate_content()
        self.assertEquals(first_article_old, self.main.latest_articles()[0].pk)
        self.assertEquals(last_article_old, self.main.latest_articles()[9].pk)

    def test_latest_rotation_no_time(self):
        site = Site.objects.get(is_default_site=True)
        settings = SettingsProxy(site)
        site_settings = settings['core']['SiteSettings']
        site_settings.m = True
        site_settings.tu = True
        site_settings.w = True
        site_settings.th = True
        site_settings.f = True
        site_settings.sa = True
        site_settings.su = True
        site_settings.content_rotation_start_date = datetime.now()
        site_settings.content_rotation_end_date = datetime.now() + timedelta(
            days=1)
        site_settings.save()

        for i in range(5):
            self.footer = FooterPage(
                title='Footer Page %s', slug='footer-page-%s' % (i, ))
            self.footer_index.add_child(instance=self.footer)

        self.assertEquals(FooterPage.objects.live().count(), 5)
        self.assertEquals(self.main.latest_articles().count(), 0)

        self.mk_articles(self.yourmind_sub, count=10, featured_in_latest=True)
        self.mk_articles(self.yourmind_sub, count=10, featured_in_latest=False)
        self.assertEquals(self.main.latest_articles().count(), 10)
        first_article_old = self.main.latest_articles()[0].pk
        last_article_old = self.main.latest_articles()[9].pk
        rotate_content()
        self.assertEquals(first_article_old, self.main.latest_articles()[0].pk)
        self.assertEquals(last_article_old, self.main.latest_articles()[9].pk)

    def test_latest_rotation_no_start_or_end_date(self):
        site = Site.objects.get(is_default_site=True)
        settings = SettingsProxy(site)
        site_settings = settings['core']['SiteSettings']
        site_settings.m = True
        site_settings.tu = True
        site_settings.w = True
        site_settings.th = True
        site_settings.f = True
        site_settings.sa = True
        site_settings.su = True
        site_settings.save()

        for i in range(5):
            self.footer = FooterPage(
                title='Footer Page %s', slug='footer-page-%s' % (i, ))
            self.footer_index.add_child(instance=self.footer)

        self.assertEquals(FooterPage.objects.live().count(), 5)
        self.assertEquals(self.main.latest_articles().count(), 0)

        self.mk_articles(self.yourmind_sub, count=10, featured_in_latest=True)
        self.mk_articles(self.yourmind_sub, count=10, featured_in_latest=False)
        self.assertEquals(self.main.latest_articles().count(), 10)
        first_article_old = self.main.latest_articles()[0].pk
        last_article_old = self.main.latest_articles()[9].pk
        rotate_content()
        self.assertEquals(first_article_old, self.main.latest_articles()[0].pk)
        self.assertEquals(last_article_old, self.main.latest_articles()[9].pk)

    def test_homepage_rotation(self):

        def get_featured_articles(section):
            return section.featured_in_homepage_articles()

        site = Site.objects.get(is_default_site=True)
        settings = SettingsProxy(site)
        site_settings = settings['core']['SiteSettings']

        site_settings.featured_in_latest_rotation = True
        d = datetime.now()
        site_settings.content_rotation_time = d.hour
        site_settings.save()

        non_rotating_articles = self.mk_articles(
            self.yourmind, count=3, featured_in_homepage=False)
        rotate_content()
        for article in non_rotating_articles:
            self.assertFalse(article.featured_in_latest)
        self.assertEquals(get_featured_articles(self.yourmind).count(), 0)
        self.yourmind_sub.featured_in_homepage_rotation = True
        self.yourmind.featured_in_homepage_rotation = False
        self.yourmind.save_revision().publish()
        self.yourmind_sub.save_revision().publish()
        self.mk_articles(
            self.yourmind_sub, count=10, featured_in_homepage=True)
        self.mk_articles(
            self.yourmind_sub, count=10, featured_in_homepage=False)
        self.assertEquals(
            get_featured_articles(self.yourmind_sub).count(), 10)
        first_article_old = get_featured_articles(self.yourmind_sub)[0].pk
        second_last_article_old = get_featured_articles(
            self.yourmind_sub)[8].pk
        last_article_old = get_featured_articles(self.yourmind_sub)[9].pk

        rotate_content()
        self.assertEquals(
            get_featured_articles(self.yourmind_sub).count(), 10)
        self.assertNotEquals(
            first_article_old, get_featured_articles(self.yourmind_sub)[0].pk)
        self.assertEquals(
            first_article_old, get_featured_articles(self.yourmind_sub)[1].pk)
        self.assertNotEquals(
            last_article_old, get_featured_articles(self.yourmind_sub)[9].pk)
        self.assertEquals(
            second_last_article_old,
            get_featured_articles(self.yourmind_sub)[9].pk)
