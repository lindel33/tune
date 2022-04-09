# Generated by Django 4.0.2 on 2022-02-26 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tune_admin', '0008_product_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_flag', models.BooleanField(default=False, verbose_name='Бронь')),
                ('sell_flag', models.BooleanField(default=False, verbose_name='Продажа')),
                ('phone', models.CharField(blank=True, max_length=13, null=True, verbose_name='Телефон')),
                ('name_user', models.CharField(blank=True, max_length=25, null=True, verbose_name='Имя клиента')),
                ('day_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('product_pka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tune_admin.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Бронь',
                'verbose_name_plural': 'Бронь',
            },
        ),
    ]
