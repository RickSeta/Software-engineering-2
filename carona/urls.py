from django.contrib import admin
from django.urls import path, include

from ride import urls as ride_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('carona/', include((ride_urls, 'ride'), namespace='ride')),
]
