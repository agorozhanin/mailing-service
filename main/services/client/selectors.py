from main.models import Client


def get_all_clients():
    """
    Получение всех клиентов
    """
    return Client.objects.all()


def get_clients_by_tag_and_code_phone(tag: str, code_phone: int):
    """
    Получение клиентов с необходимым тэгом и телефонным кодом
    """
    return Client.objects.filter(tag=tag, code_phone=code_phone)
