from django.urls import path
from .views import *

urlpatterns = [
    path('about', index, name='home'),

]