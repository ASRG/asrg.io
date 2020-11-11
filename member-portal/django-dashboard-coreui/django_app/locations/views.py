from django.shortcuts import render

from .models import Location

def location_view(request):
    context = {}
    locations = Location.objects.all()
    context['locations'] = locations
    if request.user.is_authenticated:
        return render(request, "locations/locations_authenticated.html",context)
    else:
        return render(request, "locations/locations.html",context)
