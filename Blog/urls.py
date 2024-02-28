from django.urls import path
from Blog.views import *

app_name = 'Blog'

urlpatterns = [

    path('', blog_view, name = 'home'),
    path('details/', blog_details, name = 'details'),
 
]