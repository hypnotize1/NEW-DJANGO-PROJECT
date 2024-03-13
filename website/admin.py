from django.contrib import admin
from website.models import Contact, Quote

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_date')
    list_filter = ('email',)
    search_fields = ('name', 'message')
    date_hierarchy = 'created_date'

admin.site.register(Contact, ContactAdmin)


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_date', 'message', 'phone_number')
    list_filter = ('email',)
    date_hierarchy = 'created_date'
    search_fields = ('name', 'messaage', )
    
admin.site.register(Quote,QuoteAdmin)