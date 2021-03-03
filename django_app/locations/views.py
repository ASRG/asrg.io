from django.shortcuts import render

from authentication.models import Chapter


def location_view(request):
    context = {}
    locations = Chapter.objects.all()
    context["locations"] = locations
    if request.user.is_authenticated:
        context["base_template"] = "layouts/base.html"
    else:
        context["base_template"] = "landing_page/base.html"

    return render(request, "locations/locations.html", context)
