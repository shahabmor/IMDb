from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import *

# Register your models here
admin.register(User, UserAdmin)