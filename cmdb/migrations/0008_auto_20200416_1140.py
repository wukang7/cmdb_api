# Generated by Django 2.1.10 on 2020-04-16 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0007_auto_20200416_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='server',
            name='last_mod',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='最后修改日期'),
        ),
    ]