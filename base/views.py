from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# Create your views here.
def room(request, pk):
    room = Room.objects.get(id=pk)
    return HttpResponse(room)
