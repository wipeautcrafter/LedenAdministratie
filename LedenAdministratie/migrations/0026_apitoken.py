# Generated by Django 2.1.7 on 2019-05-10 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LedenAdministratie", "0025_auto_20190416_1846"),
    ]

    operations = [
        migrations.CreateModel(
            name="APIToken",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("token_type", models.CharField(max_length=12)),
                ("token", models.CharField(max_length=32)),
            ],
        ),
    ]
