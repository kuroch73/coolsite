from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Masters


class MasterList(ListView):
    model = Masters
    template_name = 'index.html'
    context_object_name = 'masters'


class MasterDetail(DetailView):
    model = Masters
    template_name = 'master_detail.html'
