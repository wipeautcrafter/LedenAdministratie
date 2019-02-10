# Generated by Django 2.1.5 on 2019-02-10 12:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=200)),
                ('gebdat', models.DateField(verbose_name='Geboorte Datum')),
                ('geslacht', models.CharField(choices=[('m', 'M'), ('v', 'V')], default='m', max_length=1)),
                ('speltak', models.CharField(choices=[('nieuw', 'Nieuw'), ('leden', 'Leden'), ('begeleiding', 'Begeleiding'), ('bestuur', 'Bestuur')], default='nieuw', max_length=40)),
                ('email_address', models.EmailField(max_length=150, validators=[django.core.validators.EmailValidator(message='E-mail adres is ongeldig')])),
                ('straat', models.CharField(max_length=255)),
                ('postcode', models.CharField(max_length=7, validators=[django.core.validators.RegexValidator(message='De postcode is ongeldig', regex='\\d\\d\\d\\d\\s?[A-Za-z]{2}')])),
                ('woonplaats', models.CharField(max_length=100)),
                ('telnr', models.CharField(max_length=30)),
                ('mobiel', models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(message='Mobiel nummer is ongeldig', regex='06.*')])),
                ('mobiel_ouder1', models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(message='Mobiel nummer is ongeldig', regex='06.*')])),
                ('mobiel_ouder2', models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(message='Mobiel nummer is ongeldig', regex='06.*')])),
                ('email_ouder1', models.EmailField(blank=True, max_length=150)),
                ('email_ouder2', models.EmailField(blank=True, max_length=150)),
                ('aanmeld_datum', models.DateField(auto_now_add=True)),
                ('opmerkingen', models.TextField(blank=True, max_length=1024)),
            ],
            options={
                'verbose_name_plural': 'Leden',
                'ordering': ['last_name', 'first_name'],
                'permissions': (('read_lid', 'Can read leden'),),
            },
        ),
    ]
