# Generated by Django 2.1.10 on 2020-04-16 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0004_auto_20200416_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='agent',
            field=models.ForeignKey(blank=True, default=7, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.Agent', verbose_name='代理商'),
        ),
    ]
