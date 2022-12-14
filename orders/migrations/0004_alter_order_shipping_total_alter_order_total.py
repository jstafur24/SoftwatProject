# Generated by Django 4.1.1 on 2022-10-06 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_shipping_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_total',
            field=models.DecimalField(decimal_places=3, default=5000, max_digits=8),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=8),
        ),
    ]
