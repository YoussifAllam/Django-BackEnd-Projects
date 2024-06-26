# Generated by Django 5.0.2 on 2024-04-21 12:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_category_remove_category2_main_category_fk_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('Main_image', models.ImageField(upload_to='main_images/')),
                ('Cover_image', models.ImageField(upload_to='Category1_cover_images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='subproduct',
            name='category',
        ),
        migrations.RemoveField(
            model_name='productdetail',
            name='product',
        ),
        migrations.CreateModel(
            name='Category2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=30)),
                ('Product_image', models.ImageField(upload_to='Category2_Products_images/')),
                ('Is_Catogry', models.BooleanField(default=False)),
                ('Main_category_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoryes', to='products.category1', verbose_name='Category 1 Name')),
            ],
        ),
        migrations.CreateModel(
            name='Category3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=30)),
                ('Product_image', models.ImageField(upload_to='Category3_Products_images/')),
                ('category2_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoryes2', to='products.category2', verbose_name='Category 2 Name')),
            ],
        ),
        migrations.CreateModel(
            name='Category3_coverIamge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='Category3_cover_images/')),
                ('category3_fk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='categories3', to='products.category2')),
            ],
        ),
        migrations.CreateModel(
            name='Final_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=30)),
                ('Product_image', models.ImageField(upload_to='Category3_Products_images/')),
                ('category2_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories2', to='products.category2', verbose_name='Category 2 Name')),
            ],
        ),
        migrations.CreateModel(
            name='Benefits_for_Final_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Benefit', models.CharField(max_length=255)),
                ('category3_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Benefits_for_Category3', to='products.final_product')),
            ],
        ),
        migrations.CreateModel(
            name='Final_Product_For_C3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=30)),
                ('Product_image', models.ImageField(upload_to='Category3_Products_images/')),
                ('category2_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoryes31', to='products.category3', verbose_name='Category 3 Name')),
            ],
        ),
        migrations.CreateModel(
            name='Benefits_for_C3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Benefit', models.CharField(max_length=255)),
                ('category3_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Benefits_for_Final_Product_For_C3', to='products.final_product_for_c3')),
            ],
        ),
        migrations.CreateModel(
            name='grinding_for_C3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grinding_Type', models.CharField(max_length=50)),
                ('category3_fk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='grinding_for_Final_Product_For_C3', to='products.final_product_for_c3')),
            ],
        ),
        migrations.CreateModel(
            name='grinding_for_Final_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grinding_Type', models.CharField(max_length=50)),
                ('category3_fk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='grinding_for_Category3', to='products.final_product')),
            ],
        ),
        migrations.CreateModel(
            name='Weights_for_C3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Weight', models.CharField(max_length=15)),
                ('category3_fk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Weights_for_Final_Product_For_C3', to='products.final_product_for_c3')),
            ],
        ),
        migrations.CreateModel(
            name='Weights_for_Final_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Weight', models.CharField(max_length=15)),
                ('category3_fk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Weights_for_Category3', to='products.final_product')),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductDetail',
        ),
        migrations.DeleteModel(
            name='SubProduct',
        ),
    ]
