from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
        r'^api/services/oembed/',
        include('oembedservice.urls', namespace='oembedservice')
    ),
    url(
        r'^api/services/s3imageservice/',
        include('s3imageservice.urls', namespace='s3imageservice')
    ),
]
