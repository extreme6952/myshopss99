# Generated by Django 4.2.6 on 2024-11-23 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjop', '0013_alter_product_order_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marketshop',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.CharField(choices=[('PRODUCT', 'Продукт'), ('SHOP', 'Магазин')], default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CategoryMarketShop',
        ),
    ]