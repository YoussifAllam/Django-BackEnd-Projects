# Generated by Django 5.0.4 on 2024-05-02 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Startups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup_model',
            name='Startup_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
