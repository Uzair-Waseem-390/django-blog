from django.contrib import admin
from .models import *

class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'status', 'is_featured',  'created_at', 'updated_at')
    search_fields = ('title', 'short_description', 'content', 'status', 'category__category_name', 'author__username')
    list_editable = ('status', 'is_featured')

admin.site.register(Category)
admin.site.register(BlogPost, BlogPostAdmin)