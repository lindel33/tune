# Generated by Django 4.0.2 on 2022-02-23 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tune_admin', '0003_alter_product_tests'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seriescategory',
            options={'ordering': ('category',), 'verbose_name': 'Серия', 'verbose_name_plural': 'Серии'},
        ),
        migrations.AlterField(
            model_name='product',
            name='kit',
            field=models.CharField(choices=[('Без комплекта', 'Только устройство'), ('Коробка', 'Коробка'), ('Коробка, кабель Lightning — USB-C для быстрой зарядки', 'Коробка, кабель Lightning — USB-C для быстрой зарядки'), ('Кабель Lightning — USB-C для быстрой зарядки', 'Кабель Lightning — USB-C для быстрой зарядки'), ('Коробка, кабель Lightning — USB для зарядки', 'Коробка, кабель Lightning — USB для зарядки'), ('Только часы', 'Только часы'), ('Часы + зарядное устройство ', 'Часы + зарядное устройство '), ('Кабель USB‑C для быстрой зарядки Apple Watch ', 'Кабель USB‑C для быстрой зарядки Apple Watch '), ('Кабель USB для зарядки Apple Watch', 'Кабель USB для зарядки Apple Watch'), ('Полный', 'Полный')], max_length=150, verbose_name='Комплект'),
        ),
    ]
