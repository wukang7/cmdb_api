# Generated by Django 2.1.10 on 2020-04-15 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0010_auto_20200406_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='last_mod',
            field=models.DateTimeField(auto_now=True, verbose_name='最后修改日期'),
        ),
        migrations.AlterField(
            model_name='server',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='hostname',
            field=models.CharField(blank=True, max_length=128, verbose_name='主机名'),
        ),
        migrations.AlterField(
            model_name='server',
            name='sn',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='SN号'),
        ),
    ]