"""
ASGI config for project25_ORM__update__and__delete__methods__ project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project25_ORM__update__and__delete__methods__.settings')

application = get_asgi_application()
