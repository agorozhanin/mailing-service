from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls.client_api_urls')),
    path('', include('main.urls.mailing_api_urls')),
]
