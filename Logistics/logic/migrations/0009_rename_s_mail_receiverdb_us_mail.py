# Generated by Django 3.2.10 on 2023-12-24 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0008_receiverdb_s_mail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receiverdb',
            old_name='s_mail',
            new_name='us_mail',
        ),
    ]
