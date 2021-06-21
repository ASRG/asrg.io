from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.db import transaction

from .models import Training
from .filters import TrainingFilter
from .forms import TrainingForm


@login_required(login_url="/login/")
def training_postings(request):
    queryset = Training.objects.all()
    trainings = TrainingFilter(request.GET, queryset=queryset)
    return render(
        request,
        "training/training.html",
        {"trainings": trainings},
    )


@login_required(login_url="/login/")
@transaction.atomic
def training_create(request):
    errors = False
    created = False
    training_create_form = TrainingForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if training_create_form.is_valid():
            training_create_form.save()
            created = True
        else:
            errors = True
    return render(
        request,
        "training/training_create.html",
        {
            "training_create_form": training_create_form,
            "errors": errors,
            "created": created,
        },
    )
