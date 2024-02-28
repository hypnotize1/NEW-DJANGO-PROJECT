from django.urls import path
from Projects.views import *

app_name = 'Projects'

urlpatterns = [

    path('', projects_view, name = 'index'),
    path('details/', projects_detail, name = 'details'),

]