from django.shortcuts import render, redirect

from .models import Room
from .forms import RoomForm

# rooms = [
#     {"id": 1, "name": "Lets learn python!"},
#     {"id": 2, "name": "Design with me"},
#     {"id": 3, "name": "Frontend developers"},
# ]


def home(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)


def room(request, pk):
    room = Room.objects.get(pk=pk)
    context = {"room": room}
    return render(request, "base/room.html", context)


def create_room(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:home')

    context = {'room_form': form}
    return render(request, "base/room_form.html", context)


def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    context = {}
    return render(request, "base/room_form.html", context)
