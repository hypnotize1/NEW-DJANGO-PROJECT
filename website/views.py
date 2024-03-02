from django.shortcuts import render
from Blog.models import Post

# Create your views here.
def index_view(request):
    posts = Post.objects.filter(status = 1)
    return render(request, 'web/index.html',{'posts': posts})


def about_view(request):
    return render(request, 'web/about.html')



def contact_view(request):
    return render(request, 'web/contact.html')