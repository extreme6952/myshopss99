# Generated by Django 4.2.6 on 2024-11-13 22:17

from django.db import migrations
import sjop.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sjop', '0011_alter_marketshop_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='order_field',
            field=sjop.fields.OrderField(blank=True, null=True),
        ),
    ]
