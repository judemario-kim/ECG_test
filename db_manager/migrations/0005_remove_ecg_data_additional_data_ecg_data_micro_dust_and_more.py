# Generated by Django 4.0.4 on 2022-11-27 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_manager', '0004_ecg_data_additional_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ecg_data',
            name='additional_data',
        ),
        migrations.AddField(
            model_name='ecg_data',
            name='micro_dust',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='ecg_data',
            name='temperature',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='ecg_data',
            name='tmicro_dust',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='ecg_data',
            name='uv_ray',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='ecg_data',
            name='weather',
            field=models.EmailField(default='', max_length=254),
        ),
    ]