# Generated by Django 4.2.5 on 2024-01-23 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
                ('content', models.TextField(blank=True, verbose_name='описание')),
                ('master', models.ManyToManyField(to='master.masters', verbose_name='мастер')),
            ],
        ),
    ]
