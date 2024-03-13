from django import template
from Blog.models import Post
from Projects.models import Projects, Mode, ProjectImage
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('web/recent-blog.html')
def recent():
    posts = Post.objects.filter(status = 1)[:3]
    return {'posts': posts}


@register.inclusion_tag('web/our-projects.html')
def our_projects():
    now = timezone.now()
    projects = Projects.objects.filter(status = 1, published_date__lte = now)
    modes = Mode.objects.all()
    images = ProjectImage.objects.all()
    context = {'projects': projects, 'modes': modes, 'images': images}
    return context