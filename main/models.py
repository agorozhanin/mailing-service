from django.db import models


class Client(models.Model):
    """
    Сущность клиента
    """

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    id = models.AutoField(verbose_name="ID", primary_key=True, unique=True)
    phone = models.IntegerField(verbose_name="Номер телефона", null=False, blank=False)
    code_phone = models.IntegerField(verbose_name="Код мобильного оператора", null=False, blank=False)
    tag = models.CharField(verbose_name="Тэг", null=False, blank=False, max_length=255)
    time_zone = models.CharField(verbose_name="Часовой пояс", null=False, blank=False, max_length=255)

    def __str__(self):
        return f"Клиент {self.id}: {self.phone}"


class Mailing(models.Model):
    """
    Сущность рассылки
    """

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"

    id = models.AutoField(verbose_name="ID", primary_key=True, unique=True)
    start_date = models.DateTimeField(verbose_name="Дата начала", null=False, blank=False)
    end_date = models.DateTimeField(verbose_name="Дата окончания", null=False, blank=False)
    code_phone = models.IntegerField(verbose_name="Код мобильного оператора", null=False, blank=False)
    tag = models.CharField(verbose_name="Тэг", null=False, blank=False, max_length=255)
    message_text = models.TextField(verbose_name="Текст сообщения", null=False, blank=False)

    def __str__(self):
        return f"Рассылка {self.id}"


class Message(models.Model):
    """
    Сущность сообщения
    """

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    id = models.AutoField(verbose_name="ID", primary_key=True, unique=True)
    date = models.DateTimeField(verbose_name="Дата содания", null=False, blank=False)
    status = models.IntegerField(verbose_name="Статус отправки", null=True, blank=True)
    client = models.ForeignKey(to=Client, verbose_name="Клиент", on_delete=models.CASCADE)
    mailing = models.ForeignKey(to=Mailing, verbose_name="Рассылка", on_delete=models.CASCADE)

    def __str__(self):
        return f"Сообщение {self.id}"
