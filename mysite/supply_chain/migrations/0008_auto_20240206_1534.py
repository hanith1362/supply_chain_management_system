# Generated by Django 3.0.14 on 2024-02-06 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supply_chain', '0007_seller_data1_shopname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller_data1',
            old_name='product_Price',
            new_name='product_price',
        ),
    ]