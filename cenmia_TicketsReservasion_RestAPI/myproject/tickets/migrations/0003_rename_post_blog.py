# Generated by Django 5.0.2 on 2024-02-29 20:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_post'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Blog',
        ),
    ]
