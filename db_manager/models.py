from unittest.util import _MAX_LENGTH
from django.db import models
# Create your models here.

class ECG_data(models.Model):
    ecg = models.CharField(max_length = 1024)
    
    def __str__(self):
        return self.ecg

