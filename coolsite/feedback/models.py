from django.db import models

class Feedback(models.Model):
    name = models.CharField('название модели', max_length=120)
    email = models.EmailField('email', max_length=120, blank=True, null=True )
    phone = models.CharField('телефон', max_length=120,)
    description = models.CharField('описание', max_length=120, blank=True, null=True )
    call_time = models.CharField('время звонка', max_length=120,blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'форма обратной связи'
        verbose_name_plural = 'формаы обратной связи'

