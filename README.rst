========
pynetdot
========

Python client for `netdot <https://osl.uoregon.edu/redmine/projects/netdot>`_
REST API.

Netdot is an open source tool designed to help network administrators collect,
organize and maintain network documentation.

This client can query, edit, delete and create objects in a netdot installation
via it's generic REST API [https://myserver.mydomain.com/netdot/rest/]. It
exposes an interface similar to that of Django's models.

************
Installation
************

pynetdot can be installed as any other python module.

Via pip::

 pip install pynetdot

Install manually::

 python setup.py install

Pip is preferred.

*************
Configuration
*************

The library need to know the url and credentials of your netdot installation.
You may supply this at runtime by calling the setup method:

>>> import pynetdot
>>> pynetdot.setup(
....    url='http://localhost/netdot',
....    username='user',
....    password='password')

Alternately these settings can be stored in a YAML configuration file::

 username: user
 password: password
 url: http://localhost/netdot

The location of the configuration file is determined by the PYNETDOT_SETTINGS
environment variable. If this variable is not set, pynetdot will try to load
.pynetdot.yaml in users home directory.

This file will be read when you import pynetdot module.

Kerberos Single Sign-On authentication
======================================

If you are using Kerberos Single Sign-On authentication for your netdot
page, you may set your credentials like this:

>>> import pynetdot
>>> pynetdot.setup(
....    url='http://server.fqdn/netdot',
....    kerberos=True)

You will need to install requests_kerberos module first, and don't forget to
perform kinit if you are running your script on a non-Windows machine.

You can enable Kerberos SSO in a YAML configuration file as well::

 kerberos: True

*****
Usage
*****

Classes
=======

Each generic REST resource corresponds to a pynetdot class. You can get a list
of them by calling:

>>> dir(pynetdot)
['ASN',
 'ArpCache',
 'ArpCacheEntry',
 'Asset',
...

Searching
=========

Netdot's REST API is somewhat limited when filtering and searching objects.
Therefore pynetdot also doesn't offer much features in this regard.

You can get an element from netdot by its id:

>>> pynetdot.Ipblock.get(1)
pynetdot.models.Ipblock("192.168.0.0/16")

You can search by objects attributes by calling search method. You can specify
multiple attributes to match on.  This method will return a list of objects:

>>> pynetdot.Ipblock.search(address='10.0.0.0', version=4)
[pynetdot.models.Ipblock("10.0.0.0/8"), pynetdot.models.Ipblock("10.0.0.0/30")]

There is also a get_first method that will return only the first rsult (or None
if no results matched):

>>> pynetdot.Ipblock.get_first(address='10.0.0.0', version=4)
pynetdot.models.Ipblock("10.0.0.0/8")

This is useful if you know there will be only one result matching your search.

There is also the all method that will return all objects of the specified
type:

>>> pynetdot.IpblockStatus.all()
[pynetdot.models.IpblockStatus("Available"),
 pynetdot.models.IpblockStatus("Container"),
 pynetdot.models.IpblockStatus("Discovered"),
 pynetdot.models.IpblockStatus("Dynamic"),
 pynetdot.models.IpblockStatus("Reserved"),
 pynetdot.models.IpblockStatus("Static"),
 pynetdot.models.IpblockStatus("Subnet")]

Be careful when calling all on classes with many records.

Reading
=======

Pynetdot objects have attributes that match columns of records in netdot.
Attributes that link to other objects will return an instance of that type:

>>> device = pynetdot.Device.get_first(name='myrouter')
>>> device.sysname
'myrouter.localdomain'
>>> device.asset_id
pynetdot.models.Asset("Cisco 3750G-24TS CAT123456 001122334455")
>>> for interface in device.interfaces:
....    print interface.name, interface.ips
....
Vl1 []
Gi1/0/1 []
Gi1/0/2 []
Gi1/0/3 [pynetdot.models.Ipblock("10.2.2.2/32")]
Gi1/0/4 []
Gi1/0/5 []
Gi1/0/6 []
Vl200 [pynetdot.models.Ipblock("192.168.121.1/32")]
Vl202 [pynetdot.models.Ipblock("192.168.121.65/32")]
Vl668 [pynetdot.models.Ipblock("192.168.2.55/32")]

To display all attributes of an object, you can call its dump method:

>>> print device.dump()
myrouter.localdomain:
        name: myrouter.localdomain
        asset_id: Cisco 3750G-24TS CAT123456 001122334455
        aliases:
        snmp_target: 192.168.121.1/32
...

Modifying
=========

You can change the value of an objects attribute and call its save method. The
modifications will be saved back to netdot (via appropriate HTTP POST calls):

>>> ipblock = pynetdot.Ipblock.get_first(address='10.21.21.0/24')
>>> print ipblock, ipblock.description, ipblock.id
10.21.21.0/24 example block 147786909
>>> ipblock.description='hi from pynetdot'
>>> ipblock.save()
True
>>> print pynetdot.Ipblock.get(147786909).dump()
10.21.21.0/24:
        address: 10.21.21.0
        prefix: 24
        version: 4
        parent: 10.0.0.0/8
        interface: None
        vlan: None
        status: Subnet
        monitored: False
        owner: Unknown
        used_by: None
        rir:
        asn: None
        description: hi from pynetdot
        first_seen: 2016-09-28 09:36:22
        last_seen: 2016-09-28 09:36:22
        use_network_broadcast: False
        info:


If an attribute links to another pynetdot class, supply an instance of that
class:

>>> vlan = pynetdot.Vlan.get_first(vid=207)
>>> ipblock.vlan=vlan
>>> ipblock.save()
True
>>> print pynetdot.Ipblock.get(147786909).vlan.vid
207

Creating
========

Create new records in netdot by creating an instance of appropriate pynetdot
class, set its attributes and call its save method:

>>> pynetdot.Vlan.search(vid=230)
[]
>>> vlan.vid=230
>>> vlan.name="hi from pynetdot"
>>> vlan.save()
True
>>> pynetdot.Vlan.search(vid=230)
[pynetdot.models.Vlan("230")]

Deleting
========

If you call delete method on an instance of a pynetdot class the appropriate
record in netdot will be deleted:

>>> vlan=pynetdot.Vlan.get_first(vid=230)
>>> vlan.delete()
True
>>> pynetdot.Vlan.search(vid=230)
[]

Other useful info
=================

- All pynetdot classes are generated from netdot REST meta data. You can see
  this meta data by calling the URL rest/<resource>/meta_data.
- Relationships between classes can be used both ways. For example an Ipblock
  has a vlan attribute that wll return a Vlan instance and a Vlan instance has a
  subnets attribute that returns a list of Ipblock instances that reference
  this particular vlan. Call dir on object instances or see REST meta data for
  names of these relationship attributes.
- All timestamps are instances of datetime class.
