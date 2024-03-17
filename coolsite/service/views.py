from django.shortcuts import render
from django.views.generic import ListView, DetailView

from master.models import Services
from .models import Services


class ServiceList(ListView):
    model = Services
    template_name = 'service.html'
    context_object_name = 'services'


class ServiceDetail(DetailView):
    model = Services
    template_name = 'service_detail.html'
    context_object_name = 'service'