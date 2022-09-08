from django.urls import path, include

from main.views.client_views import ClientCreateAPIView, ClientUpdateDestroyAPIView

urlpatterns = [
    path('api/', include([
        path('client', ClientCreateAPIView.as_view()),
        path('client/<int:pk>', ClientUpdateDestroyAPIView.as_view()),
    ]))
]
