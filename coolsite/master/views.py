from django.shortcuts import render
from django.views.generic import ListView

from .models import Master


class Master(ListView):
    model = Master
    template_name = 'index.html'
