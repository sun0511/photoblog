from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_At', 'updated_At']

admin.site.register(Blog, BlogAdmin)