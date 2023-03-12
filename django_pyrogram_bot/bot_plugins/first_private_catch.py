import logging

from pyrogram import Client, filters
from pyrogram.types import Message

from bot.models import TelegramUser, TelegramUserHistory
from bot.utils import RunningBot

# LOGGER
logger = logging.getLogger(__name__)


@Client.on_message(filters.private, group=-9)
def catch_private(client: Client, message: Message):
    """Catch all private messages before others "on_message" """

    # Get info about running BOT
    running_bot = RunningBot()

    # if settings.DEBUG:
    #     print(message)

    # do not catch my own messages (bot) and STOP Propagation
    # This is necessary when the other thread using same session string send messages
    if message.from_user.id == running_bot.read_data()["about_bot"]["id"]:
        message.stop_propagation()
        return

    # Log activity from users
    logger.debug(
            f"🯆 {message.chat.id} - {message.from_user.id} - '@{message.from_user.username}' - '{message.from_user.first_name}' - '{message.from_user.last_name}' - '{message.text}'"
            )

    from_user = message.from_user

    tg_user, created = TelegramUser.objects.get_or_create(
            user_id=from_user.id,
            defaults={
                    'username': from_user.username,
                    'first_name': from_user.first_name,
                    'last_name': from_user.last_name,
                    }
            )

    # Record activity to Database
    TelegramUserHistory.objects.create(
            telegram_user=tg_user,
            data_received=message.text
            )
