# Generated by Django 3.2.9 on 2023-02-23 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_product_ratings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Drivetrain',
        ),
        migrations.RemoveField(
            model_name='product',
            name='height',
        ),
        migrations.RemoveField(
            model_name='product',
            name='length',
        ),
        migrations.RemoveField(
            model_name='product',
            name='maxPower',
        ),
        migrations.RemoveField(
            model_name='product',
            name='maxTorque',
        ),
        migrations.RemoveField(
            model_name='product',
            name='width',
        ),
    ]
