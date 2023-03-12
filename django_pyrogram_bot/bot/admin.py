from asgiref.sync import async_to_sync
from django.conf import settings
from django.contrib import admin
from pyrogram import Client

from .models import TelegramUser, TelegramUserHistory


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'username', 'first_name', 'last_name')

    readonly_fields = ('id', 'user_id',)

    actions = ['broadcast_message']

    @admin.action(description='Send test message')
    @async_to_sync
    async def broadcast_message(self, modeladmin, request, queryset):
        """Broadcast messages to users"""

        from .utils import RunningBot
        bot_settings = settings.PYROGRAM_BOT

        running_bot = RunningBot()
        running_bot_data = running_bot.read_data()
        if running_bot_data is None:
            print("Bot is not running or session closed")
            return

        user: TelegramUser

        async for user in queryset:
            if user.user_id != running_bot_data["about_bot"]["id"]:
                async with Client(
                        name=f"{bot_settings['BOT_NAME']}",
                        session_string=running_bot_data["session_string"],
                        no_updates=True,
                        workers=1,
                        ) as app:

                    await app.send_message(
                            chat_id=user.user_id,
                            text=f"Hello, {user.first_name}.\n This is a test message."
                            )
            else:
                continue


@admin.register(TelegramUserHistory)
class TelegramUserHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'telegram_user', 'data_received', 'timestamp')
    list_filter = ('telegram_user', 'timestamp')
