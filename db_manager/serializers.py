from rest_framework import serializers
from db_manager.models import ECG_data
from django.contrib.auth.models import User

class ECG_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ECG_data
        fields = ('ecg', 'id')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'id')