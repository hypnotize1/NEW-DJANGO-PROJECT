from datetime import time
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from Blog.models import Post, Category, Comment
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import sweetify
from Blog.forms import CommentForm

# Create your views here.
def blog_view(request, **kwargs):
    now = timezone.now()
    posts = Post.objects.filter(status = 1, published_date__lte = now)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in = [kwargs['tag_name']])
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        posts = paginator.page(1)        

    context = {'posts' : posts}

    return render(request, 'blog/blog.html', context)





def blog_details(request, pid):
     if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Submitted successfully!')
        else:
            sweetify.error(request, 'Submission failed!')
     else:
        form = CommentForm()

     now = timezone.now()
     all_posts = Post.objects.filter(status = 1, published_date__lte = now)
     current_post = get_object_or_404(all_posts, pk = pid)
     if not current_post.login_require:
        comments = Comment.objects.filter(post = current_post.id, approved = True)
        context = {'post': current_post, 'comments': comments, 'form': form}
        return render(request, 'blog/blog-details.html', context)
    
     else:
        if request.user.is_authenticated:
            comments = Comment.objects.filter(post = current_post.id, approved = True)
            context = {'post': current_post, 'comments': comments, 'form': form}
            return render(request, 'blog/blog-single.html', context)
        else:
            return HttpResponseRedirect(reverse('accounts:login'))



def blog_search(request):
    now = timezone.now() 
    posts = Post.objects.filter(status = 1, published_date__lte = now)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains = s)
    context = {'posts' : posts}
    return render(request, 'blog/blog.html', context)