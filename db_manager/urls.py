import rest_framework

from django.urls import path, include, re_path
from . import views

app_name = 'db_manager_app'

urlpatterns = [
    #path('', include(router.urls)),
    #path('ecg/', data_list),
    #path('ecg/<int:pk>', data_detail),
    path('ecg/', views.ecg_list),
    path('user/', views.user_list),
    path('user/delete/<int:pk>/', views.user_delete),
    #path('user/', user_list),
    #path('user/<int:pk>/', user_detail),
]