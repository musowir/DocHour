# Generated by Django 4.1.4 on 2022-12-23 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0013_specializations"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Specializations",
            new_name="Specialization",
        ),
    ]
