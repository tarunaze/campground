# Generated by Django 3.1.4 on 2020-12-26 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0008_auto_20201226_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]
