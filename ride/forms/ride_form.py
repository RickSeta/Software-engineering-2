from django import forms
from ride.models import Ride, Car


class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['car', 'available_seats', 'starting_hour', 'starting_point', 'destination', 'estimated_travel_time']
        widgets = {
            'available_seats': forms.NumberInput(attrs={'min': 1, 'placeholder': 'Digite o número de assentos disponíveis'}),
            'starting_hour': forms.DateTimeInput(attrs={'type':'datetime-local'}),
        }
        input_formats = {
            'starting_hour': '%Y-%m-%dT%H:%M',
        }

    def __init__(self, *args, **kwargs):
        super(RideForm, self).__init__(*args, **kwargs)
        self.fields['car'].queryset = Car.objects.filter(owner=kwargs['initial']['user'])
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
