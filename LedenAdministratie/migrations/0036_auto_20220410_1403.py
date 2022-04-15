# Generated by Django 3.2.12 on 2022-04-10 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LedenAdministratie', '0035_delete_apitoken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='dag_vrijdag',
        ),
        migrations.RemoveField(
            model_name='member',
            name='dag_zaterdag',
        ),
        migrations.AddField(
            model_name='member',
            name='days',
            field=models.IntegerField(choices=[(1, 'Vrijdag of zaterdag'), (2, 'Beide dagen')], default=1, verbose_name='Aantal dagen aanwezig'),
        ),
    ]