# Generated by Django 4.2.2 on 2023-07-03 15:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_room_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
