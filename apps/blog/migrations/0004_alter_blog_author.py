# Generated by Django 4.2.2 on 2023-07-06 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(blank=True, max_length=221, null=True),
        ),
    ]