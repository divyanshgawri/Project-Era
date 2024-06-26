# Generated by Django 5.0.6 on 2024-05-13 17:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Projects",
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
                ("name", models.CharField(max_length=30)),
                ("title", models.CharField(max_length=40)),
                ("description", models.CharField(max_length=500)),
                ("image1", models.ImageField(default="", upload_to="clients/images")),
                (
                    "image2",
                    models.ImageField(default="", upload_to="project_main/images"),
                ),
                (
                    "project_zip",
                    models.FileField(null=True, upload_to="project_main_file"),
                ),
            ],
        ),
    ]
