#!/usr/bin/env python

import pynetdot
from pprint import pprint

pynetdot.Netdot.NETDOT_URL = 'http://www.example.com/netdot/'
pynetdot.Netdot.NETDOT_USERNAME = 'admin'
pynetdot.Netdot.NETDOT_PASSWORD = 'password'

# Get products for Entity
entity = pynetdot.Entity.get_first(name='Cisco')
for p in entity.products:
    print p

# Get IP address info
ip=pynetdot.Ipblock.get_first(address='10.33.1.66')
ip.dump()
