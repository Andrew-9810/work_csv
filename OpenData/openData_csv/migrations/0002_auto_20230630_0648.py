# Generated by Django 3.2 on 2023-06-30 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openData_csv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opendata',
            name='house',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='opendata',
            name='street',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Улица'),
        ),
    ]
