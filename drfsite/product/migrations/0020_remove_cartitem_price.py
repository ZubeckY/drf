# Generated by Django 4.2.6 on 2023-11-14 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_cartitem_cart_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='price',
        ),
    ]
