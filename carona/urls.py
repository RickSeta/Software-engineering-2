from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from ride import urls as ride_urls


urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path('', include((ride_urls, 'ride'), 'ride')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
