from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView,RedirectView,
                                  UpdateView,DeleteView)

from . import models
# Create your views here.



class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School # This is return as school_list

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School # This is return as school
    template_name = 'basic_app/school_detail.html'

class IndexView(TemplateView):
    template_name = 'index.html'

    '''def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Injection"
        return context'''

class SchoolCreateView(CreateView):
    fields = ("name","principal","location")
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ("name","principal")
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
