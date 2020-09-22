from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, get_object_or_404


from .models import Events, JobPosting
from website.filters import JobPostingFilters


def landing(request):
    return render(request, "landing.html")


def about(request):
    return render(request, "about.html")


def blog(request):
    return render(request, "blog.html")


def privacy(request):
    return render(request, "privacy.html")


def security(request):
    return render(request, "security.html")


def register(request):
    response = redirect('/register/')
    return response


def events(request):
    events = Events.objects.all()
    return render(
        request,
        "events.html",
        {
            'events': events,
        },
    )


def event_details(request, event_id):
    try:
        event = Events.objects.get(id=event_id)
    except event.DoesNotExist:
        raise Http404('Event does not exist')
    return render(
        request,
        "event_detail.html",
        {
            'event': event,
        },
    )


def job_posting(request):
    queryset = JobPosting.objects.all().order_by('-date_posted')
    job_postings = JobPostingFilters(request.GET, queryset=queryset)
    return render(
        request,
        "job_posting.html",
        {
            'job_postings': job_postings,
        },
    )


def job_details(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id)
    return render(
        request,
        "job_details.html",
        {
            'job': job,
        },
    )
