from django.urls import path
from .views import *


urlpatterns = [
    path('rooms/', index, name='index'),
    path('room/<str:pk>', show, name='show'),
]
