# Generated by Django 3.2.9 on 2021-11-11 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20211111_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='url',
            field=models.TextField(default=''),
        ),
    ]
