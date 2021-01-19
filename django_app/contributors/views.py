from django.shortcuts import render

from .models import Contributor


def contributors(request):
    contributors = Contributor.objects.all()
    context = {'contributor_list': contributors}
    return render(request, 'contributors.html', context)
