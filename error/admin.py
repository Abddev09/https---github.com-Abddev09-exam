from django.contrib import admin
from .models import Error
# Register your models here.

@admin.register(Error)
class ErrorAdmin(admin.ModelAdmin):
    list_display = ('code','uz','ru','en')
    search_fields = ['code','uz','ru','en']