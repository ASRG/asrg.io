from django.shortcuts import render

from .models import Sponsor


def sponsor_view(request):
    context = {}
    sponsors = Sponsor.objects.all()
    context["sponsors"] = sponsors
    if request.user.is_authenticated:
        context["base_template"] = "layouts/base.html"
    else:
        context["base_template"] = "cms_app/base.html"

    return render(request, "sponsors/sponsors.html", context)
