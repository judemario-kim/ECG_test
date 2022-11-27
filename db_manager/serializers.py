from rest_framework import serializers
from db_manager.models import ECG_data
from db_manager.models import User_data

class ECG_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ECG_data
        fields = ('ecg', 'temperature', 'micro_dust', 'tmicro_dust', 'uv_ray', 'weather', 'ecg_user', 'created_date', 'id')
        
class User_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_data
        fields = ('email', 'password', 'id')