"""
WSGI config for Monitoring_human_health_issues_due_to_pesticides_in_agriculture project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Monitoring_human_health_issues_due_to_pesticides_in_agriculture.settings')

application = get_wsgi_application()
