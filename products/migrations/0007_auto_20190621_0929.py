# Generated by Django 2.2 on 2019-06-21 06:29

import django.core.files.storage
from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20190616_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='download',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\cipher\\project\\src\\media'), upload_to=products.models.download_loc),
        ),
    ]