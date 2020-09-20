from django.shortcuts import render
from django.http import HttpResponse

def landing(request):
    return render(request, "landing.html")

def events(request):
    return HttpResponse {'Events View'}
    #return render(request, "events.html")

def event_details(request, event_id):
    return HttpResponse {'Event Detail View = {event_id}'}
    #return render(request, "events.html")