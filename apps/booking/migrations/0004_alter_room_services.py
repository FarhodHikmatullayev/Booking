# Generated by Django 4.2.2 on 2023-06-23 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_booking_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='services',
            field=models.ManyToManyField(to='booking.roomservice'),
        ),
    ]
