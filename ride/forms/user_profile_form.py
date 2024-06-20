
from django import forms
from ride.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'degree']
        labels = {
            'degree': 'Curso',
            'profile_picture': 'Foto de Perfil',
        }
        widgets = {
            'degree': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }
