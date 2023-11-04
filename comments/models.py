from django.db import models
from django.contrib.auth.models import User
from tours.models import Tour
from datetime import datetime  
from core import settings

class Review(models.Model):  
    tours = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='comments',default=None)  
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='имя',default=None)  
    body = models.TextField(max_length=5000,default=None, verbose_name="Текст отзыва")  
    created = models.DateTimeField(default=datetime.now(), verbose_name="Создан")  
    updated = models.DateTimeField(default=datetime.now(), verbose_name="Изменен")  
    active = models.BooleanField(default=True)  
      
    class Meta:  
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ('created',)  
          
    def __str__(self):  
        return f'Comment by {self.name} on {self.tours}'