from django.shortcuts import render
from django.views.generic import ListView

from master.models import Master


class Master(ListView):
    model = Master
    template_name = 'master/index.html'
