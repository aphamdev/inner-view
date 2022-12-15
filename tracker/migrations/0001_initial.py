# Generated by Django 4.1.4 on 2022-12-14 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Interview",
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
                ("company_name", models.CharField(max_length=200)),
                ("position", models.CharField(max_length=200)),
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("notes", models.TextField()),
            ],
        ),
    ]
