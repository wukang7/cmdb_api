# Generated by Django 3.0.5 on 2020-04-05 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nic',
            name='broadcast',
            field=models.CharField(default=0, max_length=64, verbose_name='网卡广播地址'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nic',
            name='ipaddrs',
            field=models.CharField(max_length=256, verbose_name='网卡ip地址'),
        ),
        migrations.AlterField(
            model_name='nic',
            name='netmask',
            field=models.CharField(max_length=64, verbose_name='网卡掩码地址'),
        ),
    ]
