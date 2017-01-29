__version__ = '1.4.0'

from .netdot import setup, load_settings
from .models import *

settings = load_settings()
setup(url=settings['url'], username=settings['username'], password=settings['password'], kerberos=settings['kerberos'])
