# Generated by Django 4.2.11 on 2024-04-03 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agriculture_App', '0005_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.CharField(max_length=100)),
                ('feedback', models.CharField(max_length=500)),
                ('response', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'Doctor_Feedback',
            },
        ),
        migrations.CreateModel(
            name='User_Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('feedback', models.CharField(max_length=500)),
                ('response', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'User_Feedback',
            },
        ),
    ]