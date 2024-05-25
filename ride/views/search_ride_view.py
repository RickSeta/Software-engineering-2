from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.utils import timezone
from ..models import Ride, RideRequest, Place, UserProfile

class SearchRideView(TemplateView):
    template_name = 'search_ride.html'

    def get(self, request):
        # Carregar todos os lugares disponíveis para o formulário de busca
        places = Place.objects.all()
        return render(request, self.template_name, {'places': places})

    def post(self, request):
        starting_point_id = request.POST.get('starting_point')
        destination_id = request.POST.get('destination')
        starting_hour = request.POST.get('starting_hour')
        passengers = request.POST.get('passengers')

        starting_point = Place.objects.get(id=starting_point_id)
        destination = Place.objects.get(id=destination_id)

        # Converter string para objeto datetime
        starting_hour = timezone.datetime.strptime(starting_hour, '%Y-%m-%dT%H:%M')

        # Buscar caronas disponíveis
        rides = Ride.objects.filter(
            starting_point=starting_point.location,
            destination=destination.location,
            starting_hour__gte=starting_hour,
            available_seats__gte=passengers
        )

        context = {
            'starting_point': starting_point,
            'destination': destination,
            'starting_hour': starting_hour,
            'passengers': passengers,
            'search_done': True,
            'rides': rides,
            'places': Place.objects.all()  # Passar a lista de lugares novamente
        }

        # Se não houver caronas disponíveis, salve o pedido de carona
        if not rides.exists():
            user_profile = UserProfile.objects.get(user=request.user)
            ride_request = RideRequest.objects.create(
                starting_point=starting_point.location,
                destination=destination.location,
                starting_hour=starting_hour,
                created_by=user_profile
            )
            context['ride_request'] = ride_request

        return render(request, self.template_name, context)
