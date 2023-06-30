# Generated by Django 3.2 on 2023-06-29 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orgfunc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orgfunc', models.TextField(verbose_name='Деятельность организации')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=50, verbose_name='Должность')),
            ],
        ),
        migrations.CreateModel(
            name='Tipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipe', models.CharField(max_length=100, verbose_name='Тип организации')),
            ],
        ),
        migrations.CreateModel(
            name='OpenData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(verbose_name='Опубликовано')),
                ('orgname', models.TextField(verbose_name='Организация')),
                ('orgsokrname', models.TextField(verbose_name='Сокращенное наименование')),
                ('orgpubname', models.TextField(verbose_name='Публичное наименование')),
                ('rukfio', models.CharField(max_length=50, verbose_name='Должностное лицо ФИО')),
                ('index', models.CharField(max_length=6, verbose_name='Индекс')),
                ('region', models.CharField(max_length=60, verbose_name='Субъект РФ')),
                ('area', models.CharField(max_length=100, verbose_name='Область')),
                ('town', models.CharField(max_length=100, verbose_name='Город')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('house', models.CharField(max_length=20, verbose_name='Дом')),
                ('latitude', models.FloatField(max_length=8, verbose_name='Широта')),
                ('longitude', models.FloatField(max_length=8, verbose_name='Долгота')),
                ('mail', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=6, verbose_name='Номер телефона')),
                ('fax', models.CharField(max_length=6, verbose_name='Fax')),
                ('telephonedop', models.CharField(max_length=6, verbose_name='Доп. номер телефона')),
                ('url', models.CharField(max_length=200, verbose_name='URL')),
                ('okpo', models.CharField(max_length=8, verbose_name='ОКПО')),
                ('ogrn', models.CharField(max_length=14, verbose_name='ОГРН')),
                ('inn', models.CharField(max_length=10, verbose_name='ИНН')),
                ('orgfunc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openData_csv.orgfunc')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openData_csv.post')),
                ('tipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openData_csv.tipe')),
            ],
        ),
    ]
