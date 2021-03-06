"""
WSGI config for smartsheet_dropdown project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()                    #for python-dotenv method

secret_key = os.environ.get('DJANGO_SECRET1')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartsheet_dropdown.settings')

application = get_wsgi_application()
