from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm

def index(request):
    rooms = Room.objects.all()
    return HttpResponse(rooms)

def show(request, pk):
    room = Room.objects.get(id=pk)
    return HttpResponse(room)

def store(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('index')
