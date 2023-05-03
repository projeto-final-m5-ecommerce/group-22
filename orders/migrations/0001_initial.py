
# Generated by Django 4.2 on 2023-05-03 14:49



from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("ordered_time", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Order placed", "Order Placed"),
                            ("In progress", "In Progress"),
                            ("Delivered", "Delivered"),
                        ],
                        default="Order placed",
                        max_length=128,
                    ),
                ),
            ],
        ),
    ]
