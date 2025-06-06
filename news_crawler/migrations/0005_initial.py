# Generated by Django 4.2.20 on 2025-04-11 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("news_crawler", "0004_delete_news"),
    ]

    operations = [
        migrations.CreateModel(
            name="News",
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
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField()),
                ("source", models.CharField(blank=True, max_length=255)),
                ("news_url", models.URLField(unique=True)),
                ("image_url", models.URLField(unique=True)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="news_images/"),
                ),
                ("published_at", models.DateTimeField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("paragraph", models.TextField()),
            ],
        ),
    ]
