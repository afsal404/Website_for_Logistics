# Generated by Django 3.2.10 on 2023-12-20 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0004_auto_20231220_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prodb',
            name='email',
        ),
        migrations.RemoveField(
            model_name='prodb',
            name='password',
        ),
    ]
