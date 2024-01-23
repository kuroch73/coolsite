from django.db import models
from master.models import Masters

class Services (models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    content = models.TextField(blank=True, verbose_name='описание')
    master = models.ManyToManyField(Masters, verbose_name='мастер')

    def __str__(self):
        return f" - {self.name}"