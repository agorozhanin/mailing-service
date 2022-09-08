from datetime import datetime

from main.models import Client, Mailing, Message


def create_message(client: Client, mailing: Mailing):
    """
    Создание объекта сообщения со статусом 0
    для клиента
    """
    return Message.objects.create(date=datetime.now(), status=0, client=client, mailing=mailing)


def is_messages_has_sent_status(messages):
    """
    Проверка на наличие сообщений с неотправленным статусом
    """
    return True if messages.filter(status=0) is None else False
