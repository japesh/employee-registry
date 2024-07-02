# Generated by Django 4.2.3 on 2024-07-02 17:43

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "employee_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("position", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("salary", models.FloatField()),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
        ),
    ]
