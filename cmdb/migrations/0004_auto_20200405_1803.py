# Generated by Django 3.0.5 on 2020-04-05 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_auto_20200405_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nic',
            name='broadcast',
            field=models.CharField(max_length=64, null=True, verbose_name='网卡广播地址'),
        ),
    ]
