<<<<<<< HEAD
# Generated by Django 4.2 on 2023-05-03 14:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("street", models.CharField(max_length=128)),
                ("number", models.IntegerField()),
                ("city", models.CharField(max_length=128)),
                ("state", models.CharField(max_length=128)),
            ],
        ),
    ]
=======

# Generated by Django 4.2 on 2023-05-03 14:49


from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("street", models.CharField(max_length=128)),
                ("number", models.IntegerField()),
                ("city", models.CharField(max_length=128)),
                ("state", models.CharField(max_length=128)),
            ],
        ),
    ]
>>>>>>> a7fbc2bc7a8519831bf951247398d0a77c6452c6
