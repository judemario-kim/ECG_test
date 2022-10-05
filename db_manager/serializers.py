from rest_framework import serializers
from db_manager.models import ECG_data
from db_manager.models import User_data

class ECG_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ECG_data
        fields = ('ecg', 'ecg_user', 'id')
        
class User_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_data
        fields = ('email', 'password', 'id')