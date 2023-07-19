import json
import logging
from time import sleep

from django.conf import settings
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Starts Pyrogram Bot"

    def handle(self, *args, **options):
        from pyrogram import Client, idle
        from bot.apps import BotConfig
        from bot.utils import RunningBot

        # Read Bot settings
        bot_settings = settings.PYROGRAM_BOT

        # Get Client bot (client)
        client: Client = BotConfig.get_app()

        if client is None:
            print("Client Bot was not initialized")
            exit(127)

        logger.info(f"Starting Bot...")
        client.start()
        logger.info(f"Getting info about Bot..")

        about_bot = client.get_me()
        logger.info(f"Bot identified: {about_bot.id} - @{about_bot.username}")

        # Send startup message to Admins
        if bot_settings["NOTIFY_STARTUP_ADMINS"]:
            for admin in bot_settings["ADMINS"]:
                client.send_message(
                        chat_id=admin,
                        text=(f"🟢 Starting bot @{about_bot.username} - {about_bot.first_name}\n\n"
                              f"Send /admin for admin commands")
                        )
                sleep(0.1)

        running_bot = RunningBot()
        running_bot_data = {
                "session_string": str(client.export_session_string()),
                "about_bot": json.loads(str(about_bot))
                }

        # Save data of this running bot to file
        running_bot.save_data(running_bot_data)

        logger.info(f"Bot idle and Online")
        idle()
        logger.info(f"Stopping bot...")

        # Send shutdown message to Admins
        if bot_settings["NOTIFY_SHUTDOWN_ADMINS"]:
            for admin in bot_settings["ADMINS"]:
                client.send_message(
                        chat_id=admin,
                        text=f"🔴 Shutting down bot @{about_bot.username} - {about_bot.first_name}"
                        )
                sleep(0.1)

        # Delete running bot data
        running_bot.delete_data()
