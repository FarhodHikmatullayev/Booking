from django.shortcuts import render, get_object_or_404
from .models import Room, RoomReview


def room(request):
    rooms = Room.objects.order_by('-id')
    ctx = {
        "object_list": rooms
    }
    return render(request, 'booking/room.html', ctx)


def room_detail(request, slug):
    room = get_object_or_404(Room, slug=slug)
    reviews = RoomReview.objects.filter(room_id=room.id)
    ctx = {
        'object': room,
        'reviews': reviews,
    }
    return render(request, 'booking/single-room.html', ctx)


