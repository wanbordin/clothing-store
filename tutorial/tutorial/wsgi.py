"""
WSGI config for tutorial project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorial.settings')

application = get_wsgi_application()

# ----------------
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Qyun.settings")

# #application = get_wsgi_application()

# from socketio import Middleware
# from xxx.website_chat.views import sio
# django_app = get_wsgi_application()
# application = Middleware(sio, django_app)

# import eventlet
# import eventlet.wsgi
# eventlet.wsgi.server(eventlet.listen(('', 8000)), application)