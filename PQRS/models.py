from tabnanny import verbose
from unicodedata import name
from django.db import models

# Create your models here.

class Pqrs (models.Model):
   user = models.CharField(max_length=150, verbose_name='Usuario') 
   email = models.EmailField(max_length=180,verbose_name='Correo electronico')
   request_subject = models.CharField(max_length=16000, verbose_name='Asunto de la solicitud')
   message = models.TextField(verbose_name = 'Mensaje')

   def __str__(self):
      return self.user

   class Meta: 
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'Usuarios'
        ordering = ['id']
