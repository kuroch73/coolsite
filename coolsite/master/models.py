from django.db import models

class Masters(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.first_name
