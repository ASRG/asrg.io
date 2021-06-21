from django import forms

from training.models import Training
from authentication.models import Language


class TrainingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TrainingForm, self).__init__(*args, **kwargs)

    languages = forms.ModelMultipleChoiceField(
        queryset=Language.objects.all(), widget=forms.SelectMultiple
    )

    class Meta:
        model = Training
        fields = (
            "company",
            "title",
            "description",
            "costs",
            "currency",
            "duration",
            "location",
            "link",
            "logo",
            "languages",
        )
        widgets = {
            "link": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "background-color: rgba(144, 144, 144, 0.25);",
                }
            ),
        }
