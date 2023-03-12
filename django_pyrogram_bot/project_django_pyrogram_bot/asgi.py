"""
ASGI config for project_django_pyrogram_bot project_django_pyrogram_bot.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_django_pyrogram_bot.settings")

application = get_asgi_application()
