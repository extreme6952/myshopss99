# Generated by Django 4.2.6 on 2024-10-10 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjop', '0003_alter_review_unique_together_alter_review_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]