from django import forms

from .models import UserProfile
from authentication.models import Chapter

DOB_CHOICES = []
for i in range(1901, 2099):
    DOB_CHOICES.append(str(i))

class UserProfileForm(forms.ModelForm):
    # chapter = forms.ModelChoiceField(queryset=Chapter.objects.all(),label="",empty_label="Chapter",
    #     widget=forms.Select(
    #         attrs={
    #             "placeholder" : "Chapter",                
    #             "class": "form-control",
    #             "editable": False
    #         }
    #     ))
    dob = forms.DateField( required=False,
        widget=forms.SelectDateWidget(years=DOB_CHOICES,
            attrs={
                "Placeholder": 'Date of Birth',
                "class": "form-control"
            }
        )
    )
    field_of_study = forms.CharField( required=False,
        widget = forms.TextInput(
            attrs={
                "placeholder": "Field of Study",
                "class": "form-control",
                "required": False
            }
        )
    )
    bio = forms.CharField( required=False,
        widget = forms.Textarea(
            attrs={
                "placeholder": "Your short bio",
                "class": "form-control"
            }
        )
    )
    status =forms.CharField( required=False,
        widget = forms.TextInput(
            attrs={
                "placeholder": "Status message",
                "class": "form-control"
            }
        )
    )
    skills = forms.CharField( required=False,
        widget = forms.TextInput(
            attrs={
                "placeholder": "Skills",
                "class": "form-control"
            }
        )
    )
    fb_link = forms.URLField( required=False,
        widget = forms.URLInput(
            attrs={
                "placeholder": "Facebook Profile Link",
                "class": "form-control"
            }
        )
    )
    tw_link = forms.URLField( required=False,
        widget = forms.URLInput(
            attrs={
                "placeholder": "Twitter Profile Link",
                "class": "form-control"
            }
        )
    )
    ig_link = forms.URLField( required=False,
        widget = forms.URLInput(
            attrs={
                "placeholder": "Instagram Profile Link",
                "class": "form-control"
            }
        )
    )
    # pp_src = forms.ImageField(required=False,
    #     widget = forms.FileInput(
    #         attrs={
    #             "placeholder": "Avatar",
    #             "class": "form-control"
    #         }
    #     )
    # )

    class Meta:
        model = UserProfile
        fields = (
            # 'first_name', 
            # 'last_name', 
            'dob', 
            # 'gender', 
            # 'occupational_status', 
            'field_of_study', 
            # 'country', 
            'bio', 
            'status', 
            'skills', 
            'fb_link',
            'tw_link',            
            'ig_link',
            'pp_src',
            # 'profile_picture'
            )

