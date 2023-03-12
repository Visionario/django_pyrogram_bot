import logging

from django.conf import settings
from pyrogram import Client, filters
from pyrogram.types import Message

from bot.models import TelegramUser, TelegramUserHistory

# LOGGER
logger = logging.getLogger(__name__)

# Read Bot settings
bot_settings = settings.PYROGRAM_BOT


@Client.on_message(filters.command(["admin"]) & filters.private)
def cmd_admin(client: Client, message: Message, **kwargs):
    """/admin command"""
    logger.debug("basic command: cmd_admin")
    text = ("<b>Admin commands</b>\n\n"
            "/start Start\n"
            "/help Help\n"
            "/about About\n"
            "/setup Setup/Config\n"
            "/last_messages Last 10 messages received\n"
            "/last_users Last 10 listened users\n"
            "/admin This command"
            "")
    message.reply(
            text=text
            )


@Client.on_message(filters.command(["start"]) & filters.private)
def cmd_start(client: Client, message: Message, **kwargs):
    """/start command"""
    logger.debug("basic command: cmd_start")
    message.reply("Echo: /start command")


@Client.on_message(filters.command(["help"]) & filters.private)
def cmd_help(client: Client, message: Message, **kwargs):
    """/help command"""
    logger.debug("basic command: cmd_help")
    message.reply("Echo: /help command")


@Client.on_message(filters.command(["about"]) & filters.private)
def cmd_about(client: Client, message: Message, **kwargs):
    """About"""
    logger.debug("basic command: cmd_about")
    message.reply("Echo: /about command")


@Client.on_message(filters.command(["setup"]) & filters.private)
def cmd_setup(client: Client, message: Message, **kwargs):
    """Setup/Config"""
    logger.debug("basic command: cmd_setup")
    message.reply("Echo: /setup command")


@Client.on_message(filters.command(["last_messages"]) & filters.private)
def cmd_last_messages(client: Client, message: Message, **kwargs):
    """Last messages"""
    logger.debug("basic command: cmd_last_messages")

    rows = TelegramUserHistory.objects.all().order_by('-id')[:10]
    text = ''
    for row in rows:
        text = (f"{text}"
                f"{'👑 ' if row.telegram_user.user_id in bot_settings['ADMINS'] else ''}"
                f"<b>id:</b> <code>{row.telegram_user.user_id}</code>\n"
                f"<b>username:</b> @{row.telegram_user.username}\n"
                f"<b>data:</b> {row.data_received}\n\n")

    message.reply(
            text=text
            )


@Client.on_message(filters.command(["last_users"]) & filters.private)
def cmd_last_users(client: Client, message: Message, **kwargs):
    """Last users"""
    logger.debug("basic command: last_users")

    rows = TelegramUser.objects.all().order_by('-id')[:10]
    text = ''
    for row in rows:
        text = (f"{text}"
                f"{'👑 ' if row.user_id in bot_settings['ADMINS'] else ''}"
                f"<b>id:</b> <code>{row.user_id}</code>\n"
                f"<b>username:</b> @{row.username}\n"
                f"<b>first_name:</b> {row.first_name}\n"
                f"<b>last_name:</b> {row.last_name}\n\n")

    message.reply(
            text=text
            )
