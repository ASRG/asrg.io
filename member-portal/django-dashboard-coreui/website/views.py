from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect


from .models import Events


def landing(request):
    return render(request, "landing.html")


def about(request):
    return render(request, "about.html")


def blog(request):
    return render(request, "blog.html")


def privacy(request):
    return render(request, "privacy.html")


def security(request):
    return render(request, "security.html")


def projects(request):
    projects = Projects.objects.all()
    return render(request, "projects.html", {
        'projects': projects,
    })


def projects_details(request, project_id):
    try:
        project = Projects.objects.get(id=project_id)
    except project.DoesNotExist:
        raise Http404('Project does not exist')
    return render(request, "project_detail.html", {
        'project': project,
    })


def register(request):
    response = redirect('/register/')
    return response


def events(request):
    events = Events.objects.all()
    return render(request, "events.html", {
        'events': events,
    })


def event_details(request, event_id):
    try:
        event = Events.objects.get(id=event_id)
    except event.DoesNotExist:
        raise Http404('Event does not exist')
    return render(request, "event_detail.html", {
        'event': event,
    })
