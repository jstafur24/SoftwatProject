from email.policy import default
from django.db import models
from users.models import User


ShippingAddress_city = [
    (1,'Colombia' )
]


ShippingAddress_state = [
    (2,'Bogota' )
]


ShippingAddress_country = [
    (1,'Usaquen'),
    (2,'Chapinero'),
    (3,'Santa Fe'),
    (4,'San Cristobal'),
    (5,'Usme'),
    (6,'Tunjuelito'),
    (7,'Bosa'),
    (8,'Kennedy'),
    (9,'Fontibon'),
    (10,'Engativa'),
    (11,'Suba'),
    (12,'Barrios Unidos'),
    (13,'Teusaquillo'),
    (14,'Los Martires'),
    (15,'Antonio Nariño'),
    (16,'Puente Aranda'),
    (17,'Candelaria'),
    (18,'Rafale Uribe Uribe'),
    (19,'Ciudad Bolivar'),
    (20,'Sumapaz'),
]



class ShippingAddress(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    line1 = models.CharField(max_length=200)
    line2 = models.IntegerField(max_length=10)
    city = models.IntegerField(max_length=100,null=False, blank=False, choices=ShippingAddress_city)
    state = models.IntegerField(max_length=100,null=False, blank=False, choices=ShippingAddress_state)
    country = models.IntegerField(max_length=50,null=False, blank=False, choices=ShippingAddress_country)
    reference = models.CharField(max_length=300)
    codpost = models.IntegerField(max_length=10, null=False, blank=False)
    default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.codpost)

    def update_default(self, default=False):
        self.default = default
        self.save()

    @property #Para convertir un metodo en una propiedad usar
    def address(self): #propiedad
        return '{} - {} - {}' .format(self.city, self.state, self.country) 


    @property
    def shipping_address(self):
        return self.shippingaddress_set.filter(default=True).first()

    def has_shipping_address(self):
        return self.shipping_address is not None