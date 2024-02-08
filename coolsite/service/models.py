from django.db import models


class Services (models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    content = models.TextField(blank=True, verbose_name='описание')


    def __str__(self):
        return f" - {self.name}"