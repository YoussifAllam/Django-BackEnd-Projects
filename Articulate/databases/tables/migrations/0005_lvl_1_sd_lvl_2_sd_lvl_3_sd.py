# Generated by Django 5.0.2 on 2024-04-26 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0004_remove_level_1_const_word_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='lvl_1_sd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sound', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='lvl_2_sd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sound', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='lvl_3_sd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sound', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
    ]
