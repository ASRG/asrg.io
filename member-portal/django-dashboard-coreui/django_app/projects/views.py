from django.shortcuts import render

from .models import Project

def project_view(request):
    context = {}
    projects = Project.objects.all()
    context['projects'] = projects
    if request.user.is_authenticated:
        return render(request, "projects/projects_authenticated.html",context)
    else:
        return render(request, "projects/projects.html",context)

