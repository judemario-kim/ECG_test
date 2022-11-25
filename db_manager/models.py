from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models
# Create your models here.

class ECG_data(models.Model):
    ecg = models.TextField()
    ecg_user = models.EmailField(default = "")
    created_date = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return self.ecg

class User_data(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length = 16)
    