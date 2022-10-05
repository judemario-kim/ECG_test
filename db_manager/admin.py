from django.contrib import admin
from db_manager.models import ECG_data
from db_manager.models import User_data

admin.site.register(ECG_data)
admin.site.register(User_data)
# Register your models here.
