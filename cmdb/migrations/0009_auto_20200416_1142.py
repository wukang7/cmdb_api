# Generated by Django 2.1.10 on 2020-04-16 03:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0008_auto_20200416_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='create_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='创建日期'),
        ),
    ]
