# Generated by Django 3.1.4 on 2020-12-24 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customer',
            table='users',
        ),
    ]
