from django.shortcuts import render
from rest_framework import viewsets
from db_manager.models import ECG_data
from db_manager.serializers import ECG_dataSerializer
# Create your views here.

class ECG_dataViewSet(viewsets.ModelViewSet):
    queryset = ECG_data.objects.all()
    serializer_class = ECG_dataSerializer
