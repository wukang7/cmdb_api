# Generated by Django 2.1.10 on 2020-04-16 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0010_auto_20200416_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='tag',
        ),
    ]
