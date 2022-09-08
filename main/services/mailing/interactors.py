import datetime

import requests

from main.models import Message


def send_msg_to_client(message: Message, message_text: str, phone: int):
    """
    Отправляет сообщения клиентам
    при помощи стороннего API.
    В случае корректного выполнения
    проставляет сообщению статус = 1
    """
    msg_id = message.id
    data_to_send = {
        "id": msg_id,
        "phone": phone,
        "text": message_text,
    }
    token = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQxNjUwOTUsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6ImlzY2FuZGVybyJ9.bPxZKZROHIpDeUhnb0PaeXZNp2A21mno-lxiKtk66Qw'
    }
    if message.status == 0:
        response = requests.post(f"https://probe.fbrq.cloud/v1/send/{msg_id}", headers=token, json=data_to_send)

        if response.status_code == 200:
            message.status = 1
            message.date = datetime.datetime.now()
            message.save(update_fields=['status', 'date'])
