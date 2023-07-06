from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class BookingBaseModel(models.Model):
    name = models.CharField(max_length=221)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class RoomService(BookingBaseModel):
    image = models.ImageField(upload_to='rooms/services/', null=True, blank=True)


class Room(BookingBaseModel):
    slug = models.SlugField(null=True, blank=True, unique=True)
    size = models.CharField(max_length=221)
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)     # $999.99
    services = models.ManyToManyField(RoomService)
    description = RichTextField(null=True, blank=True)



class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='rooms/')



class RoomReview(BookingBaseModel):
    MARK = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reviews')
    image = models.ImageField(upload_to='rooms/reviews', null=True, blank=True)
    mark = models.IntegerField(choices=MARK)
    message = models.TextField()


class Booking(models.Model):
    client_name = models.CharField(max_length=221)
    client_phone = models.CharField(max_length=16)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings')
    check_in = models.DateField()   # 2023-07-01
    check_out = models.DateField()  # 2023-07-04
    capacity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)


    @property
    def days(self):
        days_delta = self.check_out - self.check_in
        return days_delta.days

    @property
    def total(self):
        total = self.days * self.room.price
        return total


def room_pre_save(instance, sender, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name + instance.size)


pre_save.connect(room_pre_save, sender=Room)


