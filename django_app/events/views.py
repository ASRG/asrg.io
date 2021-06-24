from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Event


def webinars_view(request):
    context = {}
    now = timezone.now()
    # events = Event.objects.all()
    events = Event.objects.filter(
        location__location="ASRG-WORLD",
        event_type__in=["Webinar", "Workshop"],
        mode="Internal",
        status__in=[2, 3, 4],
    )
    upcoming_events = events.filter(
        start_date__gte=now,
    ).order_by("start_date")
    context["upcoming_events"] = upcoming_events
    try:
        next_event = upcoming_events[0]
        context["next_event"] = next_event
    except IndexError:
        pass
    passed_events = events.filter(start_date__lt=now).order_by("-start_date")
    context["passed_events"] = passed_events
    if request.user.is_authenticated:
        context["base_template"] = "layouts/base.html"
    else:
        context["base_template"] = "cms_app/base.html"
    return render(request, "events/events.html", context)


def meetings_view(request):
    context = {}
    now = timezone.now()
    # events = Event.objects.all()
    events = Event.objects.filter(
        event_type__in=["Webinar", "Workshop"], mode="Internal", status__in=[2, 3, 4]
    ).exclude(location__location="ASRG-WORLD")
    upcoming_events = events.filter(
        start_date__gte=now,
    ).order_by("start_date")
    context["upcoming_events"] = upcoming_events
    try:
        next_event = upcoming_events[0]
        context["next_event"] = next_event
    except IndexError:
        pass
    passed_events = events.filter(
        start_date__lt=now,
    ).order_by("-start_date")
    context["passed_events"] = passed_events
    if request.user.is_authenticated:
        context["base_template"] = "layouts/base.html"
    else:
        context["base_template"] = "cms_app/base.html"
    return render(request, "events/events.html", context)


def conferences_view(request):
    context = {}
    now = timezone.now()
    # events = Event.objects.all()
    events = Event.objects.filter(
        event_type__in=["Conference"],
        status__in=[2, 3, 4],
    )
    upcoming_events = events.filter(
        start_date__gte=now,
    ).order_by("start_date")
    context["upcoming_events"] = upcoming_events
    try:
        next_event = upcoming_events[0]
        context["next_event"] = next_event
    except IndexError:
        pass
    passed_events = events.filter(start_date__lt=now).order_by("-start_date")
    context["passed_events"] = passed_events
    if request.user.is_authenticated:
        context["base_template"] = "layouts/base.html"
    else:
        context["base_template"] = "cms_app/base.html"
    return render(request, "events/events.html", context)


def ctfs_view(request):
    context = {}
    now = timezone.now()
    # events = Event.objects.all()
    events = Event.objects.filter(event_type="CTF", status__in=[2, 3, 4])
    upcoming_events = events.filter(start_date__gte=now).order_by("start_date")
    context["upcoming_events"] = upcoming_events
    try:
        next_event = upcoming_events[0]
        context["next_event"] = next_event
    except IndexError:
        pass
    passed_events = events.filter(start_date__lt=now).order_by("-start_date")
    context["passed_events"] = passed_events
    if request.user.is_authenticated:
        context["base_template"] = "layouts/base.html"
    else:
        context["base_template"] = "cms_app/base.html"
    return render(request, "events/events.html", context)


def workshop_view(request):
    context = {}
    now = timezone.now()
    # events = Event.objects.all()
    events = Event.objects.filter(event_type="Workshop", status__in=[2, 3])
    upcoming_events = events.filter(start_date__gte=now).order_by("start_date")
    context["upcoming_events"] = upcoming_events
    try:
        next_event = upcoming_events[0]
        context["next_event"] = next_event
    except IndexError:
        pass
    passed_events = events.filter(start_date__lt=now).order_by("-start_date")
    context["passed_events"] = passed_events
    if request.user.is_authenticated:
        context["base_template"] = "layouts/base.html"
    else:
        context["base_template"] = "cms_app/base.html"
    return render(request, "events/events.html", context)


def event_detail_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    context = {"event": event}
    if request.user.is_authenticated:
        context["base_template"] = "layouts/base.html"
    else:
        context["base_template"] = "cms_app/base.html"
    return render(request, "events/event_detail.html", context)
