# Generated by Django 4.0.4 on 2022-11-25 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_manager', '0003_ecg_data_created_date_ecg_data_ecg_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecg_data',
            name='additional_data',
            field=models.TextField(default=''),
        ),
    ]
