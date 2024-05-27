from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.utils import timezone
from django.http import JsonResponse
import json
from ..models import Ride, RideRequest, Place, Location, UserProfile

class SearchRideView(TemplateView):
    template_name = 'search_ride.html'

    def get(self, request):
        places = Place.objects.all()
        return render(request, self.template_name, {'places': places})

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

            #bugfix pois estava consultando po loc ao inves de coord
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
                    'car': ride.car.model,
                    'starting_hour': ride.starting_hour.strftime('%Y-%m-%d %H:%M'),
                    'available_seats': ride.available_seats,
                    'starting_point': starting_point.name,
                    'destination': destination.name
                } for ride in rides]
                return JsonResponse({'rides': rides_data})
            else:
                user_profile = UserProfile.objects.get(user=request.user)
                RideRequest.objects.create(
                    starting_point=starting_point.location,
                    destination=destination.location,
                    starting_hour=starting_hour_aware,
                    created_by=user_profile
                )
                return JsonResponse({'message': 'Ride request created successfully.'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
