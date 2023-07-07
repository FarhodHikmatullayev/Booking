from django.shortcuts import render, get_object_or_404, HttpResponse, reverse, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
import datetime
from .models import Room, RoomReview, Booking


def room(request):
    rooms = Room.objects.order_by('-id')
    checkin = request.GET.get('checkin-date')  # '2023-07-05'
    checkout = request.GET.get('checkout-date')
    adults = request.GET.get('adults')
    children = request.GET.get('children')
    data = [checkin, checkout, adults, children]

    credentials = [checkin, checkout, adults, children]
    if all(credentials):
        count_person = int(adults) + int(children)
        if checkin > checkout:
            return HttpResponse("checkout must be grater than checkin")
        checkin_lst = checkin.split('-')  # ['2023', '07', '05']
        checkin_date = datetime.date(int(checkin_lst[0]), int(checkin_lst[1]), int(checkin_lst[2]))  # 2023-07-05
        if checkin_date < datetime.datetime.today().date():
            return HttpResponse("checkin must be grater than today")
        rooms = Room.objects.filter(Q(Q(bookings__check_in__gt=checkout) |
                                      Q(bookings__check_out__lte=checkin) |
                                      Q(bookings__isnull=True)) & Q(capacity__gte=count_person))

    paginator = Paginator(rooms, 5)  # Show 5 rooms per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    data_url = f"checkin-date={checkin}&checkout-date={checkout}&adults={adults}&children={children}"
    ctx = {
        "object_list": page_obj,
        "data_url": data_url,
    }
    return render(request, 'booking/room.html', ctx)


def room_detail(request, slug):
    room = get_object_or_404(Room, slug=slug)
    reviews = RoomReview.objects.filter(room_id=room.id)
    checkout = request.GET.get('checkout-date')
    checkin = request.GET.get('checkin-date')
    adults = request.GET.get('adults')
    children = request.GET.get('children')

    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        print(checkout, checkin, adults, children)
        if adults == 'None' or children == 'None' or not checkin or not checkout:
            messages.info(request, 'firstly you should search your room')
            return redirect('booking:room')

        if name and phone:
            capacity = int(adults) + int(children)
            obj = Booking.objects.create(client_name=name, client_phone=phone, room_id=room.id, check_in=checkin,
                                         check_out=checkout, capacity=capacity)
            messages.success(request, 'You have successfully booked this room')
            return redirect('.')
        messages.info(request, 'Your name and phone number must not be empty')

    ctx = {
        'object': room,
        'reviews': reviews,
    }
    return render(request, 'booking/single-room.html', ctx)
