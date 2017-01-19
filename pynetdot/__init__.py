__version__ = '1.3.3'

from .netdot import setup, load_settings
from .models import *

settings = load_settings()
setup(url=settings['url'], username=settings['username'], password=settings['password'])
