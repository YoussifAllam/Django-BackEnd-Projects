# Generated by Django 5.0.4 on 2024-04-30 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StartUp_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('About', models.TextField(max_length=1000)),
                ('HQ_city', models.CharField(max_length=20)),
                ('HQ_country', models.CharField(max_length=20)),
                ('industry', models.CharField(max_length=30)),
                ('sub_industry', models.CharField(max_length=100)),
                ('founded', models.IntegerField()),
                ('no_of_employees', models.CharField(max_length=10)),
                ('latest_stage', models.CharField(max_length=20)),
                ('investors', models.CharField(blank=True, max_length=100, null=True)),
                ('total_raised', models.CharField(blank=True, max_length=20, null=True)),
                ('business_model', models.CharField(blank=True, max_length=30, null=True)),
                ('Startup_ID', models.IntegerField()),
                ('Extra_data', models.TextField(blank=True, max_length=1000, null=True)),
                ('Attached_files', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
