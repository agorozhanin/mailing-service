from main.models import Mailing
from main.services.message.interactors import create_message


def create_messages_to_clients(clients, mailing: Mailing):
    """
    Создание объектов сообщений со статусом 0
    для клиентов
    """
    messages = []
    for client in clients:
        messages.append(create_message(client=client, mailing=mailing))

    return messages
