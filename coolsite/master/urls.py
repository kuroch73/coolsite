from django.urls import path
from .views import *

urlpatterns = [

    path('', MasterList.as_view(), name='masters'),
    path('master/<int:pk>/', MasterDetail.as_view(), name='master'),
    ]