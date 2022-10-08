from django.db import models

from django.contrib.auth.models import AbstractUser

from orders.common import OrderStatus

# Create your models here.
class User(AbstractUser):
    def get_full_name(self):
        return '{}{}'.format(self.first_name, self.last_name)

    def orders_completed(self):
        return self.order_set.filter(status=OrderStatus.COMPLETED).order_by('-id')


class Customer(User):
    class Meta:
        proxy = True

    def get_products(self):
        return []

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()