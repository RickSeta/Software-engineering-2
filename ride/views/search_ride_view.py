from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.utils import timezone
from django.http import JsonResponse
from django.contrib import messages
import json
from ride.views.profile_view import User
from ..models import Ride, RideRequest, Place, Location, UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from ride.constants import RideStatus
from ride.mixins.google_maps_api_mixin import GoogleMapsAPIMixin



class SearchRideView(LoginRequiredMixin, GoogleMapsAPIMixin, TemplateView):
    template_name = 'search_ride.html'

    def get(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        # places = Place.objects.all()
        rides = Ride.objects.filter(available_seats__gte=1, starting_hour__gte=timezone.now(), status=RideStatus.SCHEDULED.value).exclude(car__owner=request.user.userprofile)
        context['rides'] = rides
        return render(request, self.template_name, context)

    def post(self, request):
        try:
            data = json.loads(request.body)
            starting_hour = data.get('starting_hour')
            passengers = data.get('passengers')
            starting_point_location, _ = Location.objects.get_or_create(
                latitude=data['starting_point_latitude'], longitude=data['starting_point_longitude'],
                defaults={'address': data['starting_point_address']}
            )

            destination_location, _ = Location.objects.get_or_create(
                latitude=data['destination_latitude'], longitude=data['destination_longitude'],
                defaults={'address': data['destination_address']}
            )

            starting_hour_naive = timezone.datetime.strptime(starting_hour, '%Y-%m-%dT%H:%M')
            starting_hour_aware = timezone.make_aware(starting_hour_naive, timezone.get_default_timezone())

            #filtra caronas disponíveis
            rides = Ride.objects.filter(
                starting_point=starting_point_location,
                destination=destination_location,
                starting_hour__date=starting_hour_aware.date(),
                starting_hour__hour=starting_hour_aware.hour,
                available_seats__gte=passengers,
                status=RideStatus.SCHEDULED.value
            ).exclude(car__owner=request.user.userprofile)

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
                    'starting_point': starting_point_location.address,
                    'destination': destination_location.address
                } for ride in rides]
                return JsonResponse({'rides': rides_data})
            else:
                user_profile = UserProfile.objects.get(user=request.user)
                ride_request= RideRequest.objects.create(
                    starting_point=starting_point_location,
                    destination=destination_location,
                    starting_hour=starting_hour_aware,
                    created_by=user_profile
                )
                ride_request.save()
                resp = {
                    'starting_point': starting_point_location.address,
                    'destination': destination_location.address,
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
        messages.success(request, 'Entrou na carona de {} com sucesso!'.format(ride.car.owner.user.username))
    except Exception as e:
        messages.error(request, 'Erro ao entrar na carona: {}'.format(e))
    return redirect(request.META.get('HTTP_REFERER', 'ride:search_ride'))

@login_required
def leave_ride(request, ride_id):
    try:
        ride = get_object_or_404(Ride, id=ride_id)
        user_profile = UserProfile.objects.get(user=request.user)
        ride.passengers.remove(user_profile)
        ride.available_seats += 1
        ride.save()
        messages.success(request, 'Saiu da carona de {} com sucesso!'.format(ride.car.owner.user.username))
    except Exception as e:
        messages.error(request, 'Erro ao sair da carona: {}'.format(e))
    return redirect(request.META.get('HTTP_REFERER', 'ride:search_ride'))
