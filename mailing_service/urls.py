from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls.client_api_urls')),
    path('', include('main.urls.mailing_api_urls')),
    path('', include('main.urls.statistics_api_url')),
]

urlpatterns += doc_urls
