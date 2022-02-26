# Generated by Django 3.2.6 on 2021-09-03 10:58

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_placeholderparticipation"),
    ]

    operations = [
        migrations.AddField(
            model_name="qualification",
            name="is_imported",
            field=models.BooleanField(default=True, verbose_name="imported"),
        ),
        migrations.AlterField(
            model_name="qualification",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, unique=True, verbose_name="UUID"),
        ),
        migrations.AlterField(
            model_name="qualificationcategory",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, unique=True, verbose_name="UUID"),
        ),
    ]
