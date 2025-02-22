# Generated by Django 3.2.10 on 2023-12-23 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0006_receiverdb_re_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
