# Generated by Django 4.2.4 on 2023-09-08 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttable',
            name='publish_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 9, 8, 16, 31, 25, 153808)),
        ),
    ]