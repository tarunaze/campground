# Generated by Django 3.1.4 on 2020-12-24 16:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0004_auto_20201224_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('commented_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
