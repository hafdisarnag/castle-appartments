# Generated by Django 5.2 on 2025-05-08 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_merge_20250508_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
    ]
