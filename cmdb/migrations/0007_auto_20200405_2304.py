# Generated by Django 3.0.5 on 2020-04-05 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0006_auto_20200405_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='tag',
            field=models.ManyToManyField(null=True, to='cmdb.Tag'),
        ),
    ]