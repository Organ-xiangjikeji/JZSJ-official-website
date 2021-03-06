# Generated by Django 2.0.5 on 2018-08-31 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20180831_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='datasource',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='datatype',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='industry',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='subindustry',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='名称'),
        ),
    ]
