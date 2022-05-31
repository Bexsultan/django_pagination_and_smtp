from django.db import models

class Blog(models.Model):
    date = models.DateTimeField(
        auto_now_add=True)
    
    content = models.TextField(
        db_index=True,
        blank=True,
        verbose_name='Описание')
        
    image = models.ImageField(
        upload_to='blog/',
        blank=True,
        verbose_name='Фотки')

class Email(models.Model):
    mail = models.EmailField(
        blank=True)