from django.db import models

class VacancyModel(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name