# Generated by Django 4.2.3 on 2023-11-04 15:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название тура')),
                ('distance', models.IntegerField(blank=True, null=True, verbose_name='Рассторяние от Бишкека')),
                ('price', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0, 'Цена не может быть меньше 0'), django.core.validators.MaxValueValidator(10000, 'Цена не может быть больше 10000')], verbose_name='Цена тура')),
                ('maxGroupSize', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, 'Вместимость не может быть меньше 0'), django.core.validators.MaxValueValidator(15, 'Вместимость не может быть больше 15')], verbose_name='Вместимость группы')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание тура')),
                ('photo', models.ImageField(null=True, upload_to='media/', verbose_name='Постер')),
                ('featured', models.BooleanField(default=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tours.address', verbose_name='Город, адрес')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tours.city', verbose_name='Название области')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.city'),
        ),
    ]