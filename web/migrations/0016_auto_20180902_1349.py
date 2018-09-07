# Generated by Django 2.0.5 on 2018-09-02 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_auto_20180902_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='create_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='data',
            name='update_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='industry',
            name='uid',
            field=models.CharField(max_length=10, unique=True, verbose_name='唯一标识'),
        ),
    ]