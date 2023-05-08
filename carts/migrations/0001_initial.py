# Generated by Django 4.2 on 2023-05-08 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("products", "__first__"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "total",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductsCart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("quantity", models.IntegerField(default=1)),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT, to="carts.cart"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="products.product",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="cart",
            name="cart_products",
            field=models.ManyToManyField(
                related_name="carts",
                through="carts.ProductsCart",
                to="products.product",
            ),
        ),
        migrations.AddField(
            model_name="cart",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cart",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
