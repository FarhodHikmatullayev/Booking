# Generated by Django 4.2.2 on 2023-07-03 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_room_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
