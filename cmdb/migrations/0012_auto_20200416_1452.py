# Generated by Django 2.1.10 on 2020-04-16 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0011_remove_server_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='abbreviation_name',
            field=models.CharField(max_length=32, null=True, verbose_name='缩写名'),
        ),
        migrations.AlterField(
            model_name='env',
            name='abbreviation_name',
            field=models.CharField(max_length=12, null=True, verbose_name='缩写名'),
        ),
    ]
