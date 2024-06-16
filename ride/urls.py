from django.urls import path, include

from django.conf import settings
from ride.views.create_ride_view import CreateRideView
from ride.views.profile_view import ProfileView
from django.conf.urls.static import static
from ride.views.search_ride_view import SearchRideView, join_ride
from ride.views.authetication_view import authView

app_name = 'ride'

urlpatterns = [
    path('criar/', CreateRideView.as_view(), name='create_ride'),
    path('perfil/', ProfileView.as_view(), name='profile'),
    path('buscar/', SearchRideView.as_view(), name='search_ride'),
    path('join_ride/<int:ride_id>/', join_ride, name='join_ride'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('signup/', authView, name='signup'),
]
