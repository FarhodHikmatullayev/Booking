from django.contrib import admin
from .models import Blog, Tag, Comment_blog, Category


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'slug', 'category', 'created_date')
    readonly_fields = ('created_date', 'modified_date')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Comment_blog)
class Comment_BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog', 'top_level_comment_id', 'parent_comment')
    readonly_fields = ('created_date', 'modified_date')
    search_fields = ('parent_comment_title', 'blog_title')
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'
