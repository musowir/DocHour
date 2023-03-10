# Generated by Django 4.1.4 on 2022-12-28 12:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("client", "0002_remove_client_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="uploads",
            old_name="upload",
            new_name="link",
        ),
        migrations.AddField(
            model_name="uploads",
            name="date_of_issue",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="uploads",
            name="filename",
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]
