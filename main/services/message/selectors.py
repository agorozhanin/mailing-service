from main.models import Mailing, Message


def get_all_messages_by_mailing(mailing: Mailing):
    """
    Возвращает все сообщения с необходимой рассылкой
    """
    return Message.objects.filter(mailing=mailing)
