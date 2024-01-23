from django.urls import path
from .views import *

urlpatterns = [

    path('service', ServiceList.as_view(), name='service'),

    ]