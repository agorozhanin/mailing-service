from django.urls import path, include

from main.views.statistics_views import MailingStatisticsListAPIView, MailingStatisticsRetrieveAPIView

urlpatterns = [
    path('api/', include([
        path('statistic/mailing', MailingStatisticsListAPIView.as_view()),
        path('statistic/mailing/<int:pk>', MailingStatisticsRetrieveAPIView.as_view()),
    ]))
]
