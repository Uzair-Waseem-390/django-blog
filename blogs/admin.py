from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_at', 'updated_at')

class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'status', 'is_featured',  'created_at', 'updated_at')
    search_fields = ('title', 'short_description', 'content', 'status', 'category__category_name', 'author__username')
    list_editable = ('status', 'is_featured')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'blog', 'comment', 'created_at', 'updated_at')

admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment)