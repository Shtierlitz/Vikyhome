# Generated by Django 4.2.2 on 2023-06-26 14:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cleaning", "0006_alter_service_icon_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="service",
            old_name="icon_image",
            new_name="image",
        ),
    ]
