# Generated by Django 3.1.4 on 2021-01-01 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0015_comment_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='Country',
            new_name='country',
        ),
    ]
