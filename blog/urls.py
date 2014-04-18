from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView
from blog.views import archive,hello,HomePageView,ItemsPageView,ItemDetailView,PhotoDetailView
from blog.models import Item,Photo
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
   # (r'^$',archive),
    (r'^hello/$',hello),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':'E:/myblog/static'}),
    url(r'^$',HomePageView.as_view(),name = 'index'),
    url(r'^items/$',ItemsPageView.as_view(),name = 'item_list'),
    url(r'^items/(?P<pk>\d+)/$',ItemDetailView.as_view(),name = 'item_detail'),
    url(r'^photos/(?P<pk>\d+)/$',PhotoDetailView.as_view(),name = 'photo_detail')
)