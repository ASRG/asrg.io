from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Event


def events_view(request):
    context = {}
    now = timezone.now()
    # events = Event.objects.all()
    upcoming_events = Event.objects.filter(start_date__gte=now, status=2).order_by('start_date')
    context['upcoming_events'] = upcoming_events
    try:
        next_event = upcoming_events[0]
        context['next_event'] = next_event
    except IndexError:
        pass
    passed_events = Event.objects.filter(start_date__lt=now, status=2).order_by('-start_date')
    context['passed_events'] = passed_events
    if request.user.is_authenticated:
        context['base_template'] = "layouts/base.html"
    else:
        context['base_template'] = "landing_page/base.html"
    return render(request, "events/events.html", context)


def event_detail_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    context = {"event": event}
    if request.user.is_authenticated:
        context['base_template'] = "layouts/base.html"
    else:
        context['base_template'] = "landing_page/base.html"
    return render(request, "events/event_detail.html", context)
