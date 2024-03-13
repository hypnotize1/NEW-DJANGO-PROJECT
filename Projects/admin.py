from django.contrib import admin
from Projects.models import Projects, Mode, ProjectImage
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class ProjectsAdmin(SummernoteModelAdmin):
    deate_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ['title', 'description', 'published_date', 'created_date','status']
    list_filter = ('status',)
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Mode)
admin.site.register(ProjectImage)
