from django import forms

from .models import UserProfile
from authentication.models import Chapter

class UserProfileForm(forms.ModelForm):
    # chapter = forms.ModelChoiceField(queryset=Chapter.objects.all(),label="",empty_label="Chapter",
    #     widget=forms.Select(
    #         attrs={
    #             "placeholder" : "Chapter",                
    #             "class": "form-control",
    #             "editable": False
    #         }
    #     ))

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
            'pp_src'
            )

