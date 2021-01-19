import pytz
from datetime import datetime

from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone

from authentication.models import Chapter, User
from events.models import Event


def landing(request):
    age = round((timezone.now() - datetime(2017, 7, 18, 0, 0, 0, 0, pytz.UTC)).days / 365.25, 1)
    context = {
        "members": 5657 + User.objects.exclude(chapter=None).count(),
        "locations": Chapter.objects.all().count(),
        "age": age,
        "meetings": Event.objects.all().count(),
    }
    return render(request, "landing.html", context=context)


def about(request):
    return render(request, "about.html")


def blog(request):
    return render(request, "blog.html")


def privacy(request):
    return render(request, "privacy.html")


def security(request):
    return render(request, "security.html")


def threatq(request):
    return render(request, "threatq.html")


def dashboard(request):
    return redirect('index.html')
