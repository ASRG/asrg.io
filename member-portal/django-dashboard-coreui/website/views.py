from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, get_object_or_404


from .models import JobPosting,Contributor,Announcement
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

def contributors(request):
    contributors= Contributor.objects.all()
    context = {
        'contributor_list': contributors
    }
    return render(request,'contributors.html',context)

