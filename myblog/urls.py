from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()
from django.views.generic import TemplateView
from blog.views import archive,hello,HomePageView,ItemsPageView,ItemDetailView,PhotoDetailView
from blog.models import Item,Photo
from myblog.settings import STATIC_ROOT

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':STATIC_ROOT},name = 'static'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cms/',include('cms.urls')),
    url(r'^hello/$',hello),
    url(r'^blog/$',HomePageView.as_view(),name = 'index'),
    url(r'^blog/items/$',ItemsPageView.as_view(),name = 'item_list'),
    url(r'^blog/items/(?P<pk>\d+)/$',ItemDetailView.as_view(),name = 'item_detail'),
    url(r'^blog/photos/(?P<pk>\d+)/$',PhotoDetailView.as_view(),name = 'photo_detail'),
)
