from django import template
from Blog.models import Post, Comment
from Blog.models import Category


register = template.Library()



@register.inclusion_tag('blog/blog-category.html')
def postcategory():
      cat_dt = {}
      posts = Post.objects.filter(status = 1)
      cats = Category.objects.all()
      for name in cats:
           cat_dt[name] = posts.filter(category = name).count()
      return {'categories' : cat_dt}




@register.inclusion_tag('blog/blog-latestpost.html')
def latestposts(arg = 4):
     posts = Post.objects.filter(status = 1).order_by('published_date')[:arg]
     return {'posts' : posts}



