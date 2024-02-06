from django.urls import path
from .views import *

urlpatterns = [

    path('', VacancyList.as_view(), name='vacancy'),

    ]