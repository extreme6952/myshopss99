# Generated by Django 4.2.6 on 2024-11-13 22:22

from django.db import migrations
import sjop.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sjop', '0012_product_order_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='order_field',
            field=sjop.fields.OrderField(blank=True),
        ),
    ]
