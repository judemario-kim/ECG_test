from rest_framework import serializers
from db_manager.models import ECG_data

class ECG_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ECG_data
        fields = ('ecg', 'id')