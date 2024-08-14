# orders/admin.py
from django.contrib import admin
from .models import Manager

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'name', 'is_active')
