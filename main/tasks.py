from celery import shared_task
from django_celery_beat.models import PeriodicTask

from main.services.mailing.interactors import send_msg_to_client
from main.services.mailing.selectors import get_mailing_by_id
from main.services.message.interactors import is_messages_has_sent_status
from main.services.message.selectors import get_all_messages_by_mailing


@shared_task(name='send_mailing')
def send_mailing_to_clients(instance_id):
    """
    Отправляет сообщения клиентам
    """
    instance = get_mailing_by_id(mailing_id=instance_id)
    messages = get_all_messages_by_mailing(instance)
    for msg in messages:
        send_msg_to_client(message=msg, message_text=instance.message_text, phone=msg.client.phone)

    if is_messages_has_sent_status(messages=messages):
        task = PeriodicTask.objects.get(name=f'Send mailing {instance.id}')
        task.enabled = False
        task.save()
