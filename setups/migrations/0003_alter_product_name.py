# Generated by Django 5.0.3 on 2024-12-23 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setups', '0002_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='Product', max_length=50),
        ),
    ]
