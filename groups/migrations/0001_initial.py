# Generated by Django 4.2.4 on 2023-08-08 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Groups",
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
                ("name", models.CharField(max_length=255)),
                ("group_id", models.CharField(max_length=255)),
                ("notes", models.CharField(max_length=255)),
                ("flag", models.CharField(max_length=255)),
            ],
        ),
    ]
