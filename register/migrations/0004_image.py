# Generated by Django 3.2.9 on 2023-01-29 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_alter_verifyuser_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField()),
            ],
        ),
    ]
