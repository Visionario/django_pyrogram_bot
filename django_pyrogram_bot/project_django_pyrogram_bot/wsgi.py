"""
WSGI config for project_django_pyrogram_bot project_django_pyrogram_bot.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_django_pyrogram_bot.settings")

application = get_wsgi_application()
