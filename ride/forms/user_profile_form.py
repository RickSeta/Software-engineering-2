
from django import forms
from ride.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['course', 'car', 'profile_picture']
        widgets = {
            'course': forms.TextInput(attrs={'class': 'form-control'}),
            'car': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }
