from django.contrib import admin
from .models import *
# Register your models here.

myModels = [Company]

admin.site.register(myModels)