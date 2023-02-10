# Generated by Django 3.2.7 on 2022-09-23 20:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Banner",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=60)),
                ("description", models.CharField(max_length=120)),
                ("link", models.URLField()),
                ("is_active", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
