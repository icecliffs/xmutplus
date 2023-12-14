# Generated by Django 4.2.4 on 2023-08-11 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Students",
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
                ("realname", models.CharField(max_length=255)),
                ("student_id", models.CharField(max_length=255)),
            ],
        ),
    ]