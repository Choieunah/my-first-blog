from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_fields = ['id', 'title']
    search_fields = ['title']
    
admin.site.register(Post, PostAdmin)
# Register your models here.
