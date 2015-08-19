#!/usr/bin/env python

import sys
import pynetdot
from pprint import pprint

pynetdot.Netdot.NETDOT_URL = 'http://netdot.arnes.si/netdot/'
pynetdot.Netdot.NETDOT_USERNAME = 'admin'
pynetdot.Netdot.NETDOT_PASSWORD = 'password'

d = pynetdot.Device.get_first(name='larnes6')
ifaces = pynetdot.Interface.search(name='Vl472', device=d)
for i in ifaces:
    i.dump()
    print repr(i)
sys.exit(0)

# Get products for Entity
entity = pynetdot.Entity.get_first(name='Cisco')
for p in entity.products:
    print p

# Get IP address info
ip=pynetdot.Ipblock.get_first(address='10.33.1.66')
ip.dump()
