# Generated by Django 4.2.2 on 2023-06-26 14:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cleaning", "0005_remove_extra_icon_image_service_icon_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="icon_image",
            field=models.ImageField(
                blank=True, upload_to="media/Vikyhome", verbose_name="Титульна картинка"
            ),
        ),
    ]
