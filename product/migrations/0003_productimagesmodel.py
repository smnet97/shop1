# Generated by Django 4.1.3 on 2022-12-07 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductImagesModel",
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
                ("image_1", models.ImageField(upload_to="product_images/")),
                (
                    "image_2",
                    models.ImageField(
                        blank=True, null=True, upload_to="product_images/"
                    ),
                ),
                (
                    "image_3",
                    models.ImageField(
                        blank=True, null=True, upload_to="product_images/"
                    ),
                ),
                (
                    "image_4",
                    models.ImageField(
                        blank=True, null=True, upload_to="product_images/"
                    ),
                ),
                (
                    "image_5",
                    models.FileField(blank=True, null=True, upload_to="product_files/"),
                ),
                (
                    "product",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="product.productmodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "image",
                "verbose_name_plural": "images",
            },
        ),
    ]
