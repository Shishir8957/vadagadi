# Generated by Django 3.2.9 on 2023-03-09 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_paymentcomplete_total_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.CharField(max_length=500, null=True),
        ),
    ]