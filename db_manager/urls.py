import rest_framework

from django.urls import path, include, re_path
from . import views

app_name = 'db_manager_app'
urlpatterns = [
    path('', include('rest_framework.urls', namespace='rest_framework_category')),
    path('login/', views.login, name='login'),
]