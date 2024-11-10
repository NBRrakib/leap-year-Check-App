# leapyear/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', leap_year_view, name='leap_year'),
]
