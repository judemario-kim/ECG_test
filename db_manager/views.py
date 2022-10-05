from urllib import request
from django.shortcuts import render
from rest_framework import viewsets
from db_manager.models import ECG_data
from db_manager.models import User_data
from db_manager.serializers import ECG_dataSerializer
from db_manager.serializers import User_dataSerializer

###
#from http.client import HTTPResponse
#from django.shortcuts import render
#from django.http import HttpResponse
#
#from django.contrib import auth
#from django.contrib.auth import authenticate
#from django.contrib.auth.models import User
#from django.shortcuts import render, redirect
###

# Create your views here.
class ECG_dataViewSet(viewsets.ModelViewSet):
    queryset = ECG_data.objects.all()
    serializer_class = ECG_dataSerializer
    
    
class User_dataViewSet(viewsets.ModelViewSet):
    queryset = User_data.objects.all()
    serializer_class = User_dataSerializer
    def get_queryset(self):
        qs = super().get_queryset()

        search = self.request.query_params.get('search','')
        if search:
            qs = qs.filter(email=search)
    
        return qs