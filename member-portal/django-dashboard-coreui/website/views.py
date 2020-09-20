from django.shortcuts import render
from django.http import HttpResponse, Http404


def landing(request):
    return render(request, "landing.html")


def events(request):
    events = event.objects.all{}
    return render(request, 'events.html', {
        'events': events,
    })


def event_details(request, event_id):
    try:
        event = events.objects.get(id=event_id)
    except event.DoesNotExist:
        raise Http404('Event does not exist')
    return render(request, 'event_detail.html', {
        'event': event,
    })
