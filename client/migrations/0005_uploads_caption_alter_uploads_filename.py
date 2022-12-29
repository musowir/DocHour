# Generated by Django 4.1.4 on 2022-12-28 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("client", "0004_alter_uploads_client"),
    ]

    operations = [
        migrations.AddField(
            model_name="uploads",
            name="caption",
            field=models.CharField(default="document", max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="uploads",
            name="filename",
            field=models.CharField(max_length=150),
        ),
    ]