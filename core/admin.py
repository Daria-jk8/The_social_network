from typing import Text
from django.contrib import admin

from .models import Like, Post

class LikeTabularInline(admin.TabularInline):
    
    model = Like
  
class PostAdmin(admin.ModelAdmin):
    inlines = [LikeTabularInline]

    list_display = ("title", "user", "content","updated_at")
    search_fields = ("title", )
    class Meta:
        model = Post
        

admin.site.register(Post,PostAdmin)

# admin.site.register(Like)