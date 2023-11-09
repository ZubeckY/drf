# Generated by Django 4.2.6 on 2023-11-08 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_rename_address_map_district_shop_address_district'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advantage',
            options={'ordering': ('title',), 'verbose_name': 'Преимущество', 'verbose_name_plural': 'Преимущества'},
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ('title',), 'verbose_name': 'Бренд', 'verbose_name_plural': 'Бренды'},
        ),
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины'},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'Товар в корзине', 'verbose_name_plural': 'Товары в корзинe'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='orderstatus',
            options={'ordering': ('title',), 'verbose_name': 'Статус заказа', 'verbose_name_plural': 'Статусы заказов'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('title',), 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterModelOptions(
            name='shop',
            options={'ordering': ('title',), 'verbose_name': 'Магазин', 'verbose_name_plural': 'Магазины'},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name': 'Склад', 'verbose_name_plural': 'Склады'},
        ),
        migrations.AlterModelOptions(
            name='subproduct',
            options={'ordering': ('title',), 'verbose_name': 'Подпродукт', 'verbose_name_plural': 'Подпродукты'},
        ),
        migrations.AlterField(
            model_name='product',
            name='advantages',
            field=models.ManyToManyField(blank=True, to='product.advantage'),
        ),
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, to='product.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
        migrations.AlterField(
            model_name='subproduct',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.RemoveField(
            model_name='subproduct',
            name='stock_item',
        ),
        migrations.AddField(
            model_name='subproduct',
            name='stock_item',
            field=models.ManyToManyField(blank=True, to='product.stock'),
        ),
    ]