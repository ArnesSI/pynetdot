from __future__ import absolute_import
from .netdot import setup, load_settings
from .models import *

__version__ = '1.5.1'

settings = load_settings()
setup(url=settings['url'], username=settings['username'], password=settings['password'], kerberos=settings['kerberos'])
