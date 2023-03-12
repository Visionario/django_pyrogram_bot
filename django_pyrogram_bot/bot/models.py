from django.db import models


class BaseModel(models.Model):
    """
    Base Model Class to expose Model.objects()
        (pycharm trick)
    """
    objects = models.Manager()

    class Meta:
        abstract = True


class TelegramUser(BaseModel):
    """Telegram Users"""
    objects = models.Manager()

    class Meta:
        verbose_name = 'Telegram User'
        verbose_name_plural = 'Telegram users'

    user_id = models.BigIntegerField('user_id')
    username = models.CharField('Username', max_length=32, null=True, blank=True)
    first_name = models.CharField('First Name', default="", max_length=64, null=True, blank=True)
    last_name = models.CharField('Last Name', default="", max_length=64, null=True, blank=True)

    def __str__(self):
        """STR Representation"""
        return f"{self.user_id} - @{self.username} - {self.first_name}  {self.last_name}"


class TelegramUserHistory(BaseModel):
    """Telegram Users history"""
    objects = models.Manager()

    class Meta:
        verbose_name = 'Telegram User history'
        verbose_name_plural = 'Telegram users history'

    telegram_user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, verbose_name='Telegram user', null=True, blank=True)
    data_received = models.TextField('Data received', max_length=4096, null=True, blank=True)
    timestamp = models.DateTimeField('Timestamp', auto_now_add=True, editable=False)

    def __str__(self):
        """STR Representation"""
        return f"{self.telegram_user} - {self.data_received} {self.timestamp}"
