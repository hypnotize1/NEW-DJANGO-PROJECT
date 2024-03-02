from django.urls import path
from Blog.views import *

app_name = 'Blog'

urlpatterns = [

    path('', blog_view, name = 'home'),
    path('<int:pid>', blog_details, name = 'details'),
    path('category/<str:cat_name>', blog_view, name = 'category'),
    path('author/<str:author_username>', blog_view, name = 'author'),
    path('tags/<str:tag_name>', blog_view, name = 'tags'),
    path('search/', blog_search, name = 'search'),



]