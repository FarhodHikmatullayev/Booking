# Generated by Django 4.2.2 on 2023-07-06 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_roomreview_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='booking.room'),
        ),
    ]