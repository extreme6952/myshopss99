# Generated by Django 4.2.6 on 2024-09-18 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_payment_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]