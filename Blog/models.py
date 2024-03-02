from audioop import reverse
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    image = models.ImageField(upload_to = 'blog-images/', default = 'blog-images/default.jpg')
    tags = TaggableManager()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    published_date = models.DateTimeField(null = True)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = False)
    login_require = models.BooleanField(default = False)

    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):
        return reverse('Blog:details', kwargs = {'pid': self.id})
    


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    name = models.CharField(max_length = 255)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length = 255)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-created_date']        


    def __str__(self):
        return self.name