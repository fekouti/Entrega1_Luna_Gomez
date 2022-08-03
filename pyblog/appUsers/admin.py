from django.contrib import admin
from appUsers.models import *
# Register your models here.


@admin.register(Posts)
class Posts_admin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'postContent']


@admin.register(Users)
class Users_admin(admin.ModelAdmin):
    list_display = ['name', 'email', 'password']