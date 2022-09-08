from main.models import Mailing


def get_mailing_by_id(mailing_id: int):
    """
    Возвращает рассылку по id
    """
    return Mailing.objects.filter(id=mailing_id).first()


def get_all_mailings():
    return Mailing.objects.all()
