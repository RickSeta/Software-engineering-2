from django.urls import path, include

from ride.views.index_view import IndexView
from ride.views.create_ride_view import CreateRideView
from ride.views.profile_view import ProfileView
from ride.views.ride_view import RideView
from ride.views.search_ride_view import SearchRideView, join_ride, leave_ride
from ride.views.authetication_view import authView
from ride.views.edit_profile_view import EditProfileView
from ride.views.add_car_view import add_car

app_name = 'ride'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('criar/', CreateRideView.as_view(), name='create_ride'),
    path('perfil/<int:user_id>', ProfileView.as_view(), name='profile'),
    path('perfil/editar', EditProfileView.as_view(), name='edit_profile'),
    path('buscar/', SearchRideView.as_view(), name='search_ride'),
    path('carona/<int:ride_id>/', RideView.as_view(), name='ride_detail'),
    path('join_ride/<int:ride_id>/', join_ride, name='join_ride'),
    path('leave_ride/<int:ride_id>/', leave_ride, name='leave_ride'),
    path('signup/', authView, name='signup'),
    path('perfil/addcar', add_car, name='add_car'),
]
