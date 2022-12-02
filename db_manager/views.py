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

##

from . import crawling

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

@api_view(['GET', 'POST'])
def ecg_list(request):
    
    if request.method == 'GET':
        user = request.GET.get('user', None)
        weather = request.GET.get('weather', None)
        temperature = request.GET.get('temperature', None) 
        micro_dust = request.GET.get('micro_dust', None)
        tmicro_dust = request.GET.get('tmicro_dust', None)
        uv_ray = request.GET.get('uv_ray', None)
        location = request.GET.get('location', None)

        datas = ECG_data.objects.all()
        
        if user is not None:
            datas = datas.filter(ecg_user = user)
        if weather is not None:
            datas = datas.filter(weather = weather)      
        if temperature is not None:
            datas = datas.filter(temperature = temperature)  
        if micro_dust is not None:
            datas = datas.filter(micro_dust = micro_dust)     
        if tmicro_dust is not None:
            datas = datas.filter(tmicro_dust = tmicro_dust)       
        if uv_ray is not None:
            datas = datas.filter(uv_ray = uv_ray)
        if location is not None:
            datas = datas.filter(location = location)
        print(datas)
        serialized_posts= ECG_dataSerializer(datas, many=True)
        return Response(serialized_posts.data)

    if request.method == 'POST':
        print(request.data)
        copydata = request.data.copy()
        n = copydata.pop('n', None)[0] #위도 경도
        e = copydata.pop('e', None)[0]
        data_list = crawling.crawl_weather_data(n, e)
        copydata['weather'] = data_list[0]
        copydata['temperature'] = data_list[1]
        copydata['micro_dust'] = data_list[2]
        copydata['tmicro_dust'] = data_list[3]
        copydata['uv_ray'] = data_list[4]
        copydata['location'] = data_list[5]
        '''
        위도 경도 도시받기
        도시 날씨 정보 받기
        copydata에 날씨정보 전부 넣기
        '''
        serializer = ECG_dataSerializer(data = copydata)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def user_list(request):

    if request.method == 'GET':
        email = request.GET.get('email', None)
        datas = User_data.objects.all()
        if email is not None:
            datas = datas.filter(email = email)
        serialized_posts= User_dataSerializer(datas, many=True)
        return Response(serialized_posts.data)

    if request.method == 'POST':
        print(request.data)
        serializer = User_dataSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def user_delete(request, pk):
    user = User_data.objects.get(pk=pk)
    user.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)
