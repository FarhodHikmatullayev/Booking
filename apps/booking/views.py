from django.shortcuts import render, get_object_or_404
from .models import Room, RoomReview
from django.core.paginator import Paginator


def room(request):
    rooms = Room.objects.order_by('-id')
    paginator = Paginator(rooms, 1)  # Show 1 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    ctx = {
        "object_list": page_obj
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
