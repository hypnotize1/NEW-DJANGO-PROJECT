from django.contrib import admin
from Blog.models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'status', 'login_require','published_date', 'created_date', 'author')
    list_filter = ('status', 'author')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'post', 'approved', 'created_date',)
    list_filter = ('post', 'approved')
    search_fields = ['name', 'post']

admin.site.register(Comment, CommentAdmin)