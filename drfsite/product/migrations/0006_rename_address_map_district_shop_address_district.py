# Generated by Django 4.2.6 on 2023-11-08 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_cart_options_alter_cartitem_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='address_map_district',
            new_name='address_district',
        ),
    ]