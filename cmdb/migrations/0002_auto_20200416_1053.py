# Generated by Django 2.1.10 on 2020-04-16 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='hostname',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='主机名'),
        ),
    ]