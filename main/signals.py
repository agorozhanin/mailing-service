import json

from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_beat.models import PeriodicTask, IntervalSchedule

from main.models import Mailing
from main.services.client.selectors import get_clients_by_tag_and_code_phone
from main.services.message.use_cases import create_messages_to_clients
from main.services.tasks.interators import create_base_interval_if_needed
from main.tasks import send_mailing_to_clients


@receiver(post_save, sender=Mailing)
def post_save_mailing_signal(sender, created, instance, **kwargs):
    """
    Сигнал, вызываемый сохранением рассылки
    """
    if created:
        need_clients = get_clients_by_tag_and_code_phone(tag=instance.tag, code_phone=instance.code_phone)
        create_messages_to_clients(clients=need_clients, mailing=instance)

        create_base_interval_if_needed()
        PeriodicTask.objects.create(
            name=f'Send mailing {instance.id}',
            task='send_mailing',
            interval=IntervalSchedule.objects.filter(every=10, period='seconds').first(),
            start_time=instance.start_date,
            last_run_at=instance.end_date,
            kwargs=json.dumps({"instance_id": instance.id})
        )
