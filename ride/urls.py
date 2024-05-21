from django.urls import path, include

from ride.views.create_ride_view import CreateRideView
from ride.views.profile_view import ProfileView
from ride.views.search_ride_view import SearchRideView
from ride.views.authetication_view import authView

urlpatterns = [
    path('criar/', CreateRideView.as_view(), name='create_ride'),
    path('perfil/', ProfileView.as_view(), name='profile'),
    path('buscar/', SearchRideView.as_view(), name='search_ride'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('signup/', authView, name='signup'),
]
