from django.shortcuts import render
from django.views.generic import ListView

from .models import Services


class ServiceList(ListView):
    model = Services
    template_name = 'service.html'
    context_object_name = 'services'
