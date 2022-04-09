# Generated by Django 4.0.2 on 2022-03-24 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0006_alter_ipad_memory_alter_ipad_numbers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialCharacter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_variant', models.CharField(max_length=30, verbose_name='Вариант поставщика')),
                ('new_variant', models.CharField(max_length=30, verbose_name='Вариант в прайсе')),
            ],
            options={
                'verbose_name': 'Спецификация',
                'verbose_name_plural': 'Спецификации',
            },
        ),
    ]
