# * admin *
# 사용자가 임의로 만든 my-first-blog 폴더 아래에
# startporject로 mysite를 만들고
# startapp으로 blog앱이 만들어진다.

from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_fields = ['id', 'title','created_date']
    search_fields = ['title']
    
admin.site.register(Post, PostAdmin)
# Register your models here.
