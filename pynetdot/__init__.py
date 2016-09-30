from .netdot import setup, load_settings
from .models import *
from .version import VERSION

settings = load_settings()
setup(url=settings['url'], username=settings['username'], password=settings['password'])
