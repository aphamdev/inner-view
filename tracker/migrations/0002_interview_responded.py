# Generated by Django 4.1.4 on 2022-12-14 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="interview",
            name="responded",
            field=models.BooleanField(default=False),
        ),
    ]
