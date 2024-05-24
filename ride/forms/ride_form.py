from django import forms
from ride.models import Ride, Car


class RideForm(forms.Form):

    car = forms.ModelChoiceField(queryset=Car.objects.none())
    available_seats = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'placeholder': 'Digite o número de assentos disponíveis'}))
    starting_hour = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))

    starting_point_latitude = forms.FloatField()
    starting_point_longitude = forms.FloatField()
    starting_point_address = forms.CharField(max_length=200)

    destination_latitude = forms.FloatField()
    destination_longitude = forms.FloatField()
    destination_address = forms.CharField(max_length=200)

    def __init__(self, *args, **kwargs):
        super(RideForm, self).__init__(*args, **kwargs)
        self.fields['car'].queryset = Car.objects.filter(owner=kwargs['initial']['user'])
        if not self.fields['car'].queryset.exists():
            self.fields['car'].queryset = Car.objects.none()
            self.fields['car'].help_text = 'Você não pode criar uma carona, pois não possui nenhum carro registrado.'
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
