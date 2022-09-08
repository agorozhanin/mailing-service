from django.urls import path, include

from main.views.mailing_views import MailingCreateAPIView, MailingUpdateDestroyAPIView

urlpatterns = [
    path('api/', include([
        path('mailing', MailingCreateAPIView.as_view()),
        path('mailing/<int:pk>', MailingUpdateDestroyAPIView.as_view()),
    ]))
]
