# Generated by Django 3.2.9 on 2023-01-23 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FuleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('kilometer', models.CharField(max_length=200)),
                ('fuletype', models.CharField(max_length=200)),
                ('Transmission', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('engine', models.CharField(max_length=200)),
                ('maxPower', models.CharField(max_length=200)),
                ('maxTorque', models.CharField(max_length=200)),
                ('Drivetrain', models.CharField(max_length=200)),
                ('length', models.CharField(max_length=200)),
                ('width', models.CharField(max_length=200)),
                ('height', models.CharField(max_length=200)),
                ('seatingCapacity', models.CharField(max_length=200)),
                ('fuleTankSize', models.CharField(max_length=200)),
                ('vehicleType', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='vehicleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]