#!/usr/bin/python2.7
"""
WSGI config for web_fEPSPA project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import sys
sys.path.append('/home/pilat/workspace/web_fEPSPA')
sys.path.append('/home/pilat/workspace/web_fEPSPA/')
sys.path.append('/home/pilat/workspace/fEPSP-analyser/filter_script')
sys.path.append('/home/pilat/workspace/fEPSP-analyser/filter_script/')
#sys.path.append('/home/pilat/workspace/fEPSP-analyser/filter_script/')
#sys.path.append('/home/pilat/workspace/fEPSP-analyser/filter_script/root/')
#sys.path.append('/usr/lib/python2.7/site-packages/django')
#sys.setdefaultencoding('utf-8')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_fEPSPA_config.settings")

#reload(sys)

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
