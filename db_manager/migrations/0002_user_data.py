# Generated by Django 4.0.4 on 2022-10-05 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]
