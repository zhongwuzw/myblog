from django.conf.urls import patterns, include, url
from cms.views import CmsStoryView,CmsHomeView,SearchView,CategoryView
urlpatterns = patterns('',
    url(r'^$',CmsHomeView.as_view(),name = 'cms-home'),
    url(r'^category/(?P<slug>[-\w]+)/$',CategoryView.as_view(),name = 'cms-category'),
    url(r'^search/$',SearchView.as_view(),name = 'cms-search'),
    url(r'^(?P<slug>[-\w]+)/$',CmsStoryView.as_view(),name = 'cms-story'),
)
