from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from django.http import HttpResponse
from . import models

# Create your views here.
# old way
# def index(request):
#     return render(request,"index.html")

# new
# class CBView(View):
#     def get(self,request):
#         return HttpResponse("Class Based Views are cool !")

# class IndexView(TemplateView):
#     template_name = "index.html"
#     def get_context_data(self,**kwargs):
#         context  = super().get_context_data(**kwargs)
#         context['injectme'] = "Basic Injection!"
#         return context


class IndexView(TemplateView):
    template_name = "index.html"


class SchoolListView(ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'school_list'

    # Example of making your own:
    # context_object_name = 'schools'
    model = models.School
    template_name = 'basic_app/school_list.html'

class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ("name","principal","location")
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ("name","principal")
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")