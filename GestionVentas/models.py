from django.db import models
from GestionProductos.models import Product
from django.utils.html import format_html


# Create your models here.
class Venta(models.Model):
    venta_id = models.CharField(max_length=150, verbose_name='Venta ID')
    product = models.ManyToManyField(Product) #Muchos a muchos 
    date = models.DateField(verbose_name='Fecha Venta')
    price = models.IntegerField(verbose_name='Precio')
    amount = models.IntegerField(verbose_name='Cantidad')
    image = models.ImageField(upload_to='media', null=False, blank=False, verbose_name="Imagen Producto")

    def show_image1(self):
        return format_html('<img src={} width="100" /> ', self.image.url)

    def __str__(self):
        return self.venta_id

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'Venta'
        ordering = ['id']
