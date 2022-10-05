from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class ECG_data(models.Model):
    ecg = ArrayField(models.IntegerField())
    ecg_user = models.EmailField()

    def __str__(self):
        return self.ecg

class User_data(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length = 16)
    