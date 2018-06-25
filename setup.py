from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
long_description = ''
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    l = f.readline()
    while not l.startswith('*'):
        long_description += l
        l = f.readline()

setup(
    name='pynetdot',
    version='1.5.1',

    description='Python client for netdot REST API',
    long_description=long_description,
    url='https://github.com/ArnesSI/pynetdot',
    author='Matej Vadnjal',
    author_email='matej.vadnjal@arnes.si',
    license='LGPLv3',

    packages=['pynetdot', 'pynetdot/models'],

    install_requires=['python-dateutil', 'requests', 'PyYAML', 'future'],
    requires=['dateutil', 'requests', 'yaml', 'future'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',

    ]
)
