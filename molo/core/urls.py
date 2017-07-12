from django.conf.urls import patterns, include, url
from django.views.decorators.cache import never_cache

from wagtail.utils.urlpatterns import decorate_urlpatterns

from .api.urls import api_router
from .api.views import SiteLanguagesList
from .views import (
    search, TagsListView, ReactionQuestionChoiceView,
    ReactionQuestionChoiceFeedbackView)


urlpatterns = patterns(
    '',
    url(r'^search/$', search, name='search'),
    url(
        r'^locale/(?P<locale>[\w\-\_]+)/$',
        'molo.core.views.locale_set',
        name='locale_set'
    ),
    url(
        r'^health/$',
        'molo.core.views.health',
        name='health'
    ),
    url(
        r'^home-index/$',
        'molo.core.views.home_index',
        name='home_index'
    ),
    url(
        r'^section-index/$',
        'molo.core.views.section_index',
        name='section_index'
    ),
    url(
        r'^search-index/$',
        'molo.core.views.search_index',
        name='search_index'
    ),
    url(
        r'^tag-index/$',
        'molo.core.views.tag_index',
        name='tag_index'
    ),
    url(
        r'^home-more/$',
        'molo.core.views.home_more',
        name='home_more'
    ),
    url(r'^reaction/(?P<article_slug>[0-9A-Za-z_\-]+)/'
        '(?P<question_id>\d+)/vote/$',
        ReactionQuestionChoiceView.as_view(),
        name='reaction-vote'),
    url(r'^reaction/(?P<article_slug>[0-9A-Za-z_\-]+)/'
        '(?P<question_id>\d+)/(?P<choice_slug>[0-9A-Za-z_\-]+)/feedback/$',
        ReactionQuestionChoiceFeedbackView.as_view(),
        name='reaction-feedback'),
    url(r'^import/', include(
        'molo.core.content_import.urls', namespace='content_import')),

    url(r'^api/', include(
        'molo.core.api.urls', namespace='molo_api')),

    url(r'^api/v2/', include(
        decorate_urlpatterns(api_router.get_urlpatterns(), never_cache),
        namespace=api_router.url_namespace
    )),
    url(r'^api/v2/languages/',
        SiteLanguagesList.as_view(),
        name="api-lanugages"
    ),
    url(
        r'^versions/$',
        'molo.core.views.versions',
        name='versions'),
    url(r'^djga/', include('google_analytics.urls')),
    url(
        r'^tags/(?P<tag_name>[\w-]+)/$',
        TagsListView.as_view(),
        name='tags_list'
    ),
)
