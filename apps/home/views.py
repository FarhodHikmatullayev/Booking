from django.shortcuts import render
from apps.booking.models import Room


def home(request):
    rooms = Room.objects.all()
    ctx = {
        'rooms': rooms

    }
    return render(request, 'home/index.html', ctx)


def about(request):
    ctx = {

    }
    return render(request, 'home/about.html', ctx)
