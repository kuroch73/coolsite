from django.urls import path, include
from .views import *

urlpatterns = [

    path('', Master.as_view(), name='master'),

    ]