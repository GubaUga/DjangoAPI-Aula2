# Generated by Django 3.0.8 on 2023-10-10 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20200806_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='rg',
            field=models.CharField(max_length=9, unique=True),
        ),
    ]
