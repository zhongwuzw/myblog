import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'myblog.settings'

sys.path.append('E:/myblog')
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()