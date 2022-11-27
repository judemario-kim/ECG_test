from urllib import request
from django.shortcuts import render
from rest_framework import viewsets
from db_manager.models import ECG_data
from db_manager.models import User_data
from db_manager.serializers import ECG_dataSerializer
from db_manager.serializers import User_dataSerializer

##

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import HttpResponse


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

@api_view(['GET'])
def ecg_list(request):
    user = request.GET.get('user', None)
    print("Test")
    if user is not None:
        datas = ECG_data.objects.filter(ecg_user = user)
    else:
        datas = ECG_data.objects.all()
    serialized_posts= ECG_dataSerializer(datas, many=True)
    return Response(serialized_posts.data)

@api_view(['POST'])
def ecg_post(request):
    if request.method == 'GET':
        return HttpResponse(status=200)
    if request.method == 'POST':
        print(request.data)
        serializer = ECG_dataSerializer(data = request.data, many=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data ,status=200)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_list(request):
    email = request.GET.get('email', None)
    if email is not None:
        datas = User_data.objects.filter(email = email)
    else:
        datas = User_data.objects.all()
    serialized_posts= User_dataSerializer(datas, many=True)
    return Response(serialized_posts.data)

@api_view(['POST'])
def user_post(request):
    if request.method == 'GET':
        return HttpResponse(status=200)
    if request.method == 'POST':
        print(request.data)
        serializer = User_dataSerializer(data = request.data, many=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data ,status=200)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)