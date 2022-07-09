from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

def index(request):
    rooms = Room.objects.all()
    return HttpResponse(rooms)

def show(request, pk):
    room = Room.objects.get(id=pk)
    return HttpResponse(room)
