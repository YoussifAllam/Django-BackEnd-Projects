# Generated by Django 4.2.4 on 2023-09-08 13:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('dsecription', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('is_active', models.BooleanField(default=True)),
                ('publish_date', models.DateTimeField(verbose_name=datetime.datetime.now)),
            ],
        ),
    ]
