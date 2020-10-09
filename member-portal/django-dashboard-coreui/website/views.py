from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, get_object_or_404


from .models import JobPosting, Contributor, Announcement
from authentication.models import Chapter, User
from events.models import Event
from website.filters import JobPostingFilters


def landing(request):
    context = {
        "members": User.objects.exclude(chapter=None).count(),
        "locations": Chapter.objects.all().count(),
        "age": 2.5,
        "meetings": Event.objects.all().count(),
    }
    return render(request, "landing.html", context=context)


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


@login_required(login_url="/login/")
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


@login_required(login_url="/login/")
def job_details(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id)
    return render(
        request,
        "job_details.html",
        {
            'job': job,
        },
    )


def contributors(request):
    contributors = Contributor.objects.all()
    context = {'contributor_list': contributors}
    return render(request, 'contributors.html', context)

def dashboard(request):
    response = redirect('index.html')
    return response