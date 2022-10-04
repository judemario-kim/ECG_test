from django.shortcuts import render
from rest_framework import viewsets
from db_manager.models import ECG_data
from db_manager.serializers import ECG_dataSerializer
from db_manager.serializers import UserSerializer
from django.contrib.auth.models import User

###
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
#
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



###
# Create your views here.
class ECG_dataViewSet(viewsets.ModelViewSet):
    queryset = ECG_data.objects.all()
    serializer_class = ECG_dataSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/usermanagement')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')