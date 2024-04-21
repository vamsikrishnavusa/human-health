# Generated by Django 4.2.11 on 2024-04-01 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agriculture_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('Address', models.CharField(default=None, max_length=100, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'UserDetails',
            },
        ),
    ]
