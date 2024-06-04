from django.contrib import admin
from django.urls import path, include

from ride import urls as ride_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include((ride_urls, 'ride'), 'ride')),
]
