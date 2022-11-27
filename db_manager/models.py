from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models

from django.utils import timezone
# Create your models here.

class ECG_data(models.Model):
    ecg = models.TextField()
    #additional_data = models.TextField(default="")
    temperature = models.CharField(max_length = 15)
    micro_dust = models.CharField(max_length = 15)
    tmicro_dust = models.CharField(max_length = 15)
    uv_ray = models.CharField(max_length = 15)
    weather = models.CharField(max_length = 15)
    ecg_user = models.EmailField(default = "")
    created_date = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.ecg_user

class User_data(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length = 16)
    
