# Generated by Django 4.2.5 on 2024-02-08 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_rename_master_services_masters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='masters',
        ),
    ]
