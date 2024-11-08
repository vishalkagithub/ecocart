# Generated by Django 5.1.1 on 2024-09-20 12:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(max_length=30, null=True)),
                ('category_picture', models.ImageField(null=True, upload_to='static/category/')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_register',
            fields=[
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('Pincode', models.CharField(max_length=20, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('address', models.TextField(null=True)),
                ('picture', models.ImageField(upload_to='static/userpic/')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_picture', models.ImageField(null=True, upload_to='static/slider/')),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField(null=True)),
                ('discount', models.IntegerField(null=True)),
                ('quantity', models.CharField(max_length=20, null=True)),
                ('product_image', models.ImageField(null=True, upload_to='static/product/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.tbl_category')),
            ],
        ),
    ]