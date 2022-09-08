from django_celery_beat.models import IntervalSchedule


def create_base_interval_if_needed():
    if IntervalSchedule.objects.filter(every=10, period='seconds').first():
        IntervalSchedule.objects.create(every=10, period='seconds')
