from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Master


class MasterList(ListView):
    model = Master
    template_name = 'index.html'
    context_object_name = 'masters'


class MasterDetail(DetailView):
    model = Master
    template_name = 'master_detail.html'
