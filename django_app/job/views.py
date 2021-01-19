from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404

from .models import JobPosting
from .filters import JobPostingFilters


@login_required(login_url="/login/")
def job_posting(request):
    queryset = JobPosting.objects.all().order_by('-date_posted')
    # job_postings = JobPostingFilters(request.GET, queryset=queryset)
    return render(
        request,
        "job_posting.html",
        {'job_postings': None},  # job_postings,
    )


@login_required(login_url="/login/")
def job_details(request, pk):
    job = get_object_or_404(JobPosting, pk=pk)
    return render(
        request,
        "job_details.html",
        {
            'job': job,
        },
    )
