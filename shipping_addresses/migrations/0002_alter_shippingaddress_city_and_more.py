# Generated by Django 4.1.1 on 2022-10-07 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_addresses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='city',
            field=models.IntegerField(choices=[(1, 'Colombia')], max_length=100),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='codpost',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='country',
            field=models.IntegerField(choices=[(1, 'Usaquen'), (2, 'Chapinero'), (3, 'Santa Fe'), (4, 'San Cristobal'), (5, 'Usme'), (6, 'Tunjuelito'), (7, 'Bosa'), (8, 'Kennedy'), (9, 'Fontibon'), (10, 'Engativa'), (11, 'Suba'), (12, 'Barrios Unidos'), (13, 'Teusaquillo'), (14, 'Los Martires'), (15, 'Antonio Nariño'), (16, 'Puente Aranda'), (17, 'Candelaria'), (18, 'Rafale Uribe Uribe'), (19, 'Ciudad Bolivar'), (20, 'Sumapaz')], max_length=50),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='line2',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='state',
            field=models.IntegerField(choices=[(1, 'Bogota')], max_length=100),
        ),
    ]