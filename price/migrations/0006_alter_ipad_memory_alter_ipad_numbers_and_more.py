# Generated by Django 4.0.2 on 2022-03-24 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0005_ipad_macbook_macbook1_watch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipad',
            name='memory',
            field=models.TextField(help_text='16,16гб,16 gb,16 гб...', verbose_name='Память'),
        ),
        migrations.AlterField(
            model_name='ipad',
            name='numbers',
            field=models.TextField(help_text='iPad 12.iPad 9,iPad 11', verbose_name='Полное название'),
        ),
        migrations.AlterField(
            model_name='ipad',
            name='series',
            field=models.TextField(help_text='iPad pro,iPad mini...', verbose_name='Модели с префиксом'),
        ),
        migrations.AlterField(
            model_name='macbook',
            name='memory',
            field=models.TextField(help_text='16gb,16гб,16 gb,16 гб...', verbose_name='Память'),
        ),
        migrations.AlterField(
            model_name='macbook',
            name='series',
            field=models.TextField(help_text='MacBook Pro,MacBook Air...', verbose_name='Модели с префиксом'),
        ),
        migrations.AlterField(
            model_name='macbook1',
            name='names',
            field=models.TextField(help_text='M1', verbose_name='Extra'),
        ),
        migrations.AlterField(
            model_name='macbook1',
            name='series',
            field=models.TextField(help_text='MacBook Pro,MacBook Air...', verbose_name='Модели с префиксом'),
        ),
    ]
