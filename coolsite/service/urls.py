from django.urls import path
from .views import *

urlpatterns = [

    path('', ServiceList.as_view(), name='service'),
    path('<int:pk>/', ServiceDetail.as_view(), name='services')

    ]