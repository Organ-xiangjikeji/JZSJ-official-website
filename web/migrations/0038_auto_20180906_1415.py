# Generated by Django 2.0.5 on 2018-09-06 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0037_auto_20180906_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='needs',
            field=models.TextField(blank=True, max_length=3072, null=True, verbose_name='需求'),
        ),
    ]