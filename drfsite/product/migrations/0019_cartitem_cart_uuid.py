# Generated by Django 4.2.6 on 2023-11-14 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_remove_cartitem_cart_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='cart_uuid',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
