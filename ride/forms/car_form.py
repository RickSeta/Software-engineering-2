from django import forms
from ride.models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['model', 'year', 'color', 'plate']
        labels = {
            'model': 'Modelo',
            'year': 'Ano',
            'color': 'Cor',
            'plate': 'Placa',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'plate': forms.TextInput(attrs={'class': 'form-control'}),
        }