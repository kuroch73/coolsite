from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Masters
from service.models import Services


class MasterList(ListView):
    model = Masters
    template_name = 'index.html'
    context_object_name = 'masters'
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['services'] = {}
        for master in context['masters']:
            context['services'][master.id] = Services.objects.filter(masters=master)
        print(context)
        return context

class MasterDetail(DetailView):
    model = Masters
    template_name = 'master_detail.html'
