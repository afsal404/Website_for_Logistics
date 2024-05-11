# Generated by Django 3.2.10 on 2023-11-24 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='receiverdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('re_f_name', models.CharField(blank=True, max_length=100, null=True)),
                ('re_mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('re_address', models.CharField(blank=True, max_length=100, null=True)),
                ('re_date', models.DateField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='senderdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('se_f_name', models.CharField(blank=True, max_length=100, null=True)),
                ('se_mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('se_address', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
