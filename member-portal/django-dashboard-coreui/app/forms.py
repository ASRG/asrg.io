from django import forms

from .models import UserProfile

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'dob', 'gender', 'occupational_status', 'field_of_study', 'chapter', 'country', 'bio', 'status',
                    'skills', 'profile_picture')