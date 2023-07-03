# Generated by Django 4.2.2 on 2023-07-03 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_room_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomreview',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='booking.room'),
            preserve_default=False,
        ),
    ]