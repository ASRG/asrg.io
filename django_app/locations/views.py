from django.shortcuts import render

from .models import Location
from authentication.models import Chapter

def location_view(request):
    context = {}
    locations = Chapter.objects.all()
    context['locations'] = locations
    if request.user.is_authenticated:
        return render(request, "locations/locations_authenticated.html",context)
    else:
        return render(request, "locations/locations.html",context)
