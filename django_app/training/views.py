from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404

from .models import Training
from .filters import TrainingFilter


@login_required(login_url="/login/")
def training_postings(request):
    queryset = Training.objects.all()
    trainings = TrainingFilter(request.GET, queryset=queryset)
    return render(
        request,
        "training/training.html",
        {"trainings": trainings},
    )
