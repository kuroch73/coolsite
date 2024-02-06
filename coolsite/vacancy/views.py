from django.views.generic import ListView

from .models import VacancyModel

class VacancyList(ListView):
    model = VacancyModel
    template_name = 'vacancy.html'
    context_object_name = 'vacancys'

