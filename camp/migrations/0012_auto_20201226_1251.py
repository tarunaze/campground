# Generated by Django 3.1.4 on 2020-12-26 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('camp', '0011_family'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='family',
            name='head',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='place',
            name='added_by',
            field=models.ManyToManyField(related_name='added_place', through='camp.Add', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='place',
            name='rated_by',
            field=models.ManyToManyField(related_name='rated_place', through='camp.Rating', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='place',
            name='visited_by',
            field=models.ManyToManyField(related_name='visited_place', through='camp.Visited', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='visited',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]