# Generated by Django 5.0.6 on 2024-06-12 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_manage', '0002_remove_product_sku_product_discounted_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='product_description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='discounted_price',
            new_name='product_discounted_price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='original_price',
            new_name='product_original_price',
        ),
    ]
