# Generated by Django 5.0.2 on 2024-03-24 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('Main_image', models.ImageField(upload_to='main_images/')),
            ],
        ),
    ]
