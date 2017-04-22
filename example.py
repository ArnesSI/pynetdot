#!/usr/bin/env python

from __future__ import print_function
import pynetdot

pynetdot.setup(url='https://myserver.mydomain.com/netdot/', username='admin', password='password')

# Get interface by name on specific device
device = pynetdot.Device.get_first(name='myrouter')
ifaces = pynetdot.Interface.search(name='Vl400', device=device)
for i in ifaces:
    print(i.dump())
    print(repr(i))

# Get products for Entity
entity = pynetdot.Entity.get_first(name='Cisco')
for p in entity.products:
    print(p)

# Get IP address info
ip=pynetdot.Ipblock.get_first(address='10.33.1.66')
print(ip.dump())
