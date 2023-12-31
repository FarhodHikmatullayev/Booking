from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=221)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
