# Generated by Django 3.1.4 on 2021-01-11 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0021_auto_20210110_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='isSelected',
            field=models.BooleanField(default=False),
        ),
    ]
