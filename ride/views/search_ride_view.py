from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.utils import timezone
from django.http import JsonResponse
from django.contrib import messages
import json
from ride.views.profile_view import User
from ..models import Ride, RideRequest, Place, Location, UserProfile

class SearchRideView(TemplateView):
    template_name = 'search_ride.html'

    def get(self, request):
        places = Place.objects.all()
        rides = Ride.objects.filter(available_seats__gte=1, starting_hour__gte=timezone.now())
        return render(request, self.template_name, {'places': places, 'rides': rides})

    def post(self, request):
        try:
            data = json.loads(request.body)
            starting_point_name = data.get('starting_point')
            destination_name = data.get('destination')
            starting_point_coords = data.get('starting_point_coords').split(', ')
            destination_coords = data.get('destination_coords').split(', ')
            starting_hour = data.get('starting_hour')
            passengers = data.get('passengers')

            #bugfix pois estava achando multiplos results
            starting_point_location = Location.objects.filter(
                latitude=starting_point_coords[0], longitude=starting_point_coords[1]
            ).first()
            if not starting_point_location:
                starting_point_location = Location.objects.create(
                    latitude=starting_point_coords[0], longitude=starting_point_coords[1]
                )

            destination_location = Location.objects.filter(
                latitude=destination_coords[0], longitude=destination_coords[1]
            ).first()
            if not destination_location:
                destination_location = Location.objects.create(
                    latitude=destination_coords[0], longitude=destination_coords[1]
                )

            #bugfix pois estava consultando por loc ao inves de coord
            starting_point = Place.objects.filter(
                location=starting_point_location
            ).first()
            if not starting_point:
                starting_point = Place.objects.create(
                    name=starting_point_name, location=starting_point_location
                )

            destination = Place.objects.filter(
                location=destination_location
            ).first()
            if not destination:
                destination = Place.objects.create(
                    name=destination_name, location=destination_location
                )

            starting_hour_naive = timezone.datetime.strptime(starting_hour, '%Y-%m-%dT%H:%M')
            starting_hour_aware = timezone.make_aware(starting_hour_naive, timezone.get_default_timezone())

            #filtra caronas disponíveis
            rides = Ride.objects.filter(
                starting_point=starting_point.location,
                destination=destination.location,
                starting_hour__date=starting_hour_aware.date(),  
                starting_hour__hour=starting_hour_aware.hour,    
                available_seats__gte=passengers
            )

            if rides.exists():
                rides_data = [{
                    'id': ride.id,
                    'is_passenger': request.user.userprofile in ride.passengers.all(),
                    'car': str(ride.car),
                    'car_color': ride.car.color,
                    'owner': ride.car.owner.user.username,
                    'owner_rating': ride.car.owner.rating,
                    'starting_hour': ride.starting_hour,
                    'available_seats': ride.available_seats,
                    'starting_point': starting_point.name,
                    'destination': destination.name
                } for ride in rides]
                return JsonResponse({'rides': rides_data})
            else:
                user_profile = UserProfile.objects.get(user=request.user)
                ride_request= RideRequest.objects.create(
                    starting_point=starting_point.location,
                    destination=destination.location,
                    starting_hour=starting_hour_aware,
                    created_by=user_profile
                )
                ride_request.save()
                resp = {
                    'starting_point': starting_point.name,
                    'destination': destination.name,
                    'starting_hour': starting_hour_aware,
                    'created_by': user_profile.user.username
                }
                return JsonResponse({'message': 'Ride request created successfully.', 'ride_request': resp}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@login_required
def join_ride(request, ride_id):
    try:
        ride = get_object_or_404(Ride, id=ride_id)
        if ride.available_seats == 0:
            messages.error(request, 'Não foi possível entrar na carona pois ela já está cheia!')
            return redirect('ride:search_ride')
        user_profile = UserProfile.objects.get(user=request.user)
        ride.passengers.add(user_profile)
        ride.available_seats -= 1
        ride.save()
        messages.success(request, 'Entrou na carona do {} com sucesso!'.format(ride.car.owner.user.username))
    except Exception as e:
        messages.error(request, 'Erro ao entrar na carona: {}'.format(e))
    return redirect('ride:search_ride')