# Generated by Django 2.0.5 on 2018-09-02 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_auto_20180902_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='head',
            field=models.FileField(blank=True, null=True, upload_to='media/heads/', verbose_name='文件头图'),
        ),
        migrations.AlterField(
            model_name='data',
            name='file',
            field=models.FileField(upload_to='media/datas/', verbose_name='文件地址'),
        ),
    ]
