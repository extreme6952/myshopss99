# Generated by Django 4.2.6 on 2024-10-10 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjop', '0007_rating_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
