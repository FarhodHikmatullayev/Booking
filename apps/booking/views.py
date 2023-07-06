from django.shortcuts import render, get_object_or_404, HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
import datetime
from .models import Room, RoomReview


def room(request):
    rooms = Room.objects.order_by('-id')
    checkin = request.GET.get('checkin-date')   # '2023-07-05'
    checkout = request.GET.get('checkout-date')
    adults = request.GET.get('adults')
    children = request.GET.get('children')

    if checkin > checkout:
        return HttpResponse("checkout must be grater than checkin")
    checkin_lst = checkin.split('-')    # ['2023', '07', '05']
    checkin_date = datetime.date(int(checkin_lst[0]), int(checkin_lst[1]), int(checkin_lst[2]))  # 2023-07-05
    if checkin_date < datetime.datetime.today().date():
        return HttpResponse("checkin must be grater than today")

    credentials = [checkin, checkout, adults, children]
    if all(credentials):
        rooms = Room.objects.filter(Q(bookings__check_in__gt=checkout) |
                                    Q(bookings__check_out__lte=checkin) |
                                    Q(bookings__isnull=True))

    paginator = Paginator(rooms, 5)  # Show 5 rooms per page.
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
