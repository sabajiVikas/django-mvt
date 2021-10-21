from django.contrib import admin
from .models import Hiretuber

class Hire(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email', 'tuber_name')
    list_display_links = ('id', 'first_name')

admin.site.register(Hiretuber, Hire)
