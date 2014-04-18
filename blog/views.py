from django.shortcuts import render,render_to_response
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.template import RequestContext
from blog.models import Item,Photo
# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self,**kwargs):
        context = super(HomePageView,self).get_context_data(**kwargs)
        context['item_list'] = Item.objects.all()
        return context
    
class ItemsPageView(ListView):
    template_name = "items_list.html"
    model = Item
    context_object_name = "items_list"
    
class ItemDetailView(DetailView):
    template_name = 'items_detail.html'
    model = Item
    context_object_name = 'item_detail'
    
class PhotoDetailView(DetailView):
    template_name = 'photos_detail.html'
    model = Photo
    context_object_name = 'photo_detail'
   # queryset = Item.objects.all()
    
    
def archive(request):
    print "shit"
    return render_to_response('archive.html')
def hello(request):
    return render_to_response('Hello.html')