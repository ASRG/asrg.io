from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, get_object_or_404


<<<<<<< HEAD
from .models import Events
from .models import Projects
=======
from .models import JobPosting,Contributor
from website.filters import JobPostingFilters
>>>>>>> 22238dbe0b9611bb2dcb7369df3fb5de65329562


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


def projects(request):
    projects = Projects.objects.all()
    return render(request, "projects.html", {
        'projects': projects,
    })


def project_details(request, project_id):
    try:
        project = Projects.objects.get(id=project_id)
    except project.DoesNotExist:
        raise Http404('Project does not exist')
    return render(request, "project_detail.html", {
        'project': project,
    })


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