# Generated by Django 3.1.7 on 2021-03-19 16:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import ephios.extra.json


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_remove_event_mail_updates"),
    ]

    operations = [
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("slug", models.SlugField(max_length=255)),
                ("failed", models.BooleanField(default=False)),
                (
                    "data",
                    models.JSONField(
                        blank=True,
                        decoder=ephios.extra.json.CustomJSONDecoder,
                        default=dict,
                        encoder=ephios.extra.json.CustomJSONEncoder,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="affected user",
                    ),
                ),
            ],
        ),
    ]
