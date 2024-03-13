from django.shortcuts import render
from Projects.models import Projects, Mode, ProjectImage
from django.utils import timezone
from django.http import Http404

# Create your views here.
def projects_view(request, **kwargs):
    now = timezone.now()
    projects = Projects.objects.filter(status = 1, published_date__lte = now)
    modes = Mode.objects.all()
    images = ProjectImage.objects.all()
    context = {'projects': projects, 'modes': modes, 'images': images}
    return render(request, 'projects/projects.html', context)


def projects_detail(request, pid):
    try:
        project = Projects.objects.get(pk = pid)
    except Projects.DoesNotExist:
        raise Http404("Project not found")
    images = project.images.all()
    context = {'project': project, 'images': images}
    return render(request, 'projects/project-details.html', context)