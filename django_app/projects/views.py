from django.shortcuts import render

from .models import Project


def project_view(request):
    context = {}
    projects = Project.objects.all()
    context['projects'] = projects
    if request.user.is_authenticated:
        context['base_template'] = "layouts/base.html"
    else:
        context['base_template'] = "landing_page/base.html"

    return render(request, "projects/projects.html", context)
