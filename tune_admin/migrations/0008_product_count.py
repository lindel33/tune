# Generated by Django 4.0.2 on 2022-02-23 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tune_admin', '0007_product_name_tmp'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count',
            field=models.SmallIntegerField(default=0, verbose_name='Счетчик сохранений'),
        ),
    ]
