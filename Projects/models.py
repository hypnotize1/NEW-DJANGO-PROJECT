from django.db import models
from django.urls import reverse
from Blog.models import Category

class Mode(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class ProjectImage(models.Model):
    image = models.ImageField(upload_to = 'projects/')


# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ManyToManyField(ProjectImage, blank = True)
    # image = models.ImageField(upload_to = 'projects/' ,default = 'projects/default.jpg')
    status = models.BooleanField(default = False)
    category = models.ManyToManyField(Category)
    published_date = models.DateTimeField(null = True)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    mode = models.ForeignKey(Mode, on_delete = models.CASCADE)

        
    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ['-created_date']


    def get_absolute_url(self):
        return reverse('Projects:details', kwargs = {'pid': self.id})
    

