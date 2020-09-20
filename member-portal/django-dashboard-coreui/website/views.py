from django.shortcuts import render
from django.http import HttpResponse

def landing(request):
    return render(request, "landing.html")

def events(request):
    return HttpResponse ('<p>Events View</p>')
    #return render(request, "events.html")

def event_details(request, event_id):
    return HttpResponse (f'<p>Event Detail View = {event_id}</p>')
    #return render(request, "events.html")