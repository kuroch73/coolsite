from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *
from service.models import Services


class MasterList(ListView):
    model = Assemble
    template_name = 'index.html'
    context_object_name = 'assembles'



class MasterDetail(DetailView):
    model = Masters
    template_name = 'master_detail.html'
    context_object_name = 'master'
