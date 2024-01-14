from django.urls import path, include
from .views import *

urlpatterns = [
    path('about/', include('about.urls')),
    path('', Master.as_view(), name='master'),

    ]