# Generated by Django 4.2 on 2023-05-03 13:42

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("products", "0001_initial"),
        ("carts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="cart_products",
            field=models.ManyToManyField(related_name="carts", to="products.product"),
        ),
    ]
