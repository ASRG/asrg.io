from django.shortcuts import render,get_object_or_404
from django.utils import timezone

from .models import Event

def events_view(request):
    context = {}
    now = timezone.now()
    # events = Event.objects.all()
    upcoming_events = Event.objects.filter(start_date__gte=now).order_by('start_date')
    context['upcoming_events'] = upcoming_events
    try:
        next_event = upcoming_events[0]
        context['next_event'] = next_event
    except IndexError:
        pass
    passed_events = Event.objects.filter(start_date__lt=now).order_by('-start_date')
    context['passed_events'] = passed_events
    if request.user.is_authenticated:
        return render(request, "events_authenticated_users.html",context)
    else:
        return render(request, "events.html",context)



def event_detail_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user.is_authenticated:
        return render (request, "event_detail_authenticated_users.html", {
        'event': event,
    })
    else:
        return render (request, "event_detail.html", {
        'event': event,
    })
