from django.urls import path
from .views import *


urlpatterns = [

    path('room/<str:pk>', room, name='room')
]
