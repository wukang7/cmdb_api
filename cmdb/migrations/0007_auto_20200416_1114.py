# Generated by Django 2.1.10 on 2020-04-16 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0006_auto_20200416_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessunit',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='businessunit',
            name='manager',
        ),
    ]
