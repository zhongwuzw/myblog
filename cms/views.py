from django.shortcuts import render,render_to_response,get_object_or_404
from cms.models import Story,Category
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import View,TemplateView
from django.db.models import Q
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# def search(request):
#     if 'q' in request.POST:
#         term = request.POST['q']
#         story_list = Story.objects.filter(Q(title__contains = term) | Q(markdown_content__contains=term))
#         heading = 'Search results'
#     return render_to_response('story_list.html',locals(),context_instance = RequestContext(request))

class SearchView(View):
#     @csrf_exempt
#     def dispatch(self,*args,**kwargs):
#         return super(SearchView,self).dispatch(*args,**kwargs)
    
    def post(self,request):
        if 'q' in request.POST:
            term = request.POST['q']
            story_list = Story.objects.filter(Q(title__contains = term) | Q(markdown_content__contains = term))
            heading = 'Search results'
        return render(request,'story_list.html',locals())
#         return render_to_response('story_list.html',locals())

class CategoryView(TemplateView):
    template_name = 'story_list.html'
    
    def get_context_data(self, **kwargs):
        print self.request
        print self.args
        print self.kwargs
        
        context = super(CategoryView,self).get_context_data(**kwargs)
        category = get_object_or_404(Category,slug = kwargs['slug'])
        context['category'] = category
        context['story_list'] = Story.objects.filter(category = category)
        context['heading'] = "Category:%s" %category.label
        return context
#     
# def category(request,slug):
#     category = get_object_or_404(Category,slug = slug)
#     story_list = Story.objects.filter(category = category)
#     heading = "Category:%s" % category.label
#     return render_to_response('story_list.html',locals())
#   
class CmsStoryView(DetailView):   
    template_name = 'story_detail.html'
    model = Story
    context_object_name = 'story'
    
class CmsHomeView(ListView):
    template_name = 'story_list.html'
    model = Story
    context_object_name = 'story_list'