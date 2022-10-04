from django.shortcuts import render
from rest_framework import viewsets
from db_manager.models import ECG_data
from db_manager.serializers import ECG_dataSerializer
from db_manager.serializers import UserSerializer
from django.contrib.auth.models import User
# Create your views here.

class ECG_dataViewSet(viewsets.ModelViewSet):
    queryset = ECG_data.objects.all()
    serializer_class = ECG_dataSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer