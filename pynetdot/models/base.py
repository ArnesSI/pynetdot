import pynetdot.netdot as n
import pynetdot.fields as f
import pynetdot.models

class BaseArpCache(n.Netdot):
    '''
    Device ARP Cache
    '''
    resource = 'ArpCache/'
    id_field = 'id'
    _fields = [
        f.LinkField('device', display_name='Device', link_to='Device'),
        f.DateTimeField('tstamp', display_name='Timestamp'),
    ]
    _views = {'all': ['tstamp', 'device'], 'brief': ['tstamp', 'device']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['tstamp', 'device']])
        return l.strip()

    @property
    def entries(self):
        cls = getattr(pynetdot.models, 'ArpCacheEntry')
        return cls.search(arpcache=self.id)


class BaseArpCacheEntry(n.Netdot):
    '''
    ARP Cache Entry
    '''
    resource = 'ArpCacheEntry/'
    id_field = 'id'
    _fields = [
        f.LinkField('arpcache', display_name='ARP Cache', link_to='ArpCache'),
        f.LinkField('interface', display_name='Interface', link_to='Interface'),
        f.LinkField('ipaddr', display_name='IP', link_to='Ipblock'),
        f.LinkField('physaddr', display_name='Physical Address', link_to='PhysAddr'),
    ]
    _views = {'all': ['interface', 'ipaddr', 'physaddr', 'arpcache'], 'brief': ['ipaddr', 'physaddr', 'interface']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['ipaddr', 'physaddr', 'interface']])
        return l.strip()


class BaseASN(n.Netdot):
    '''
    Autonomous System Number
    '''
    resource = 'ASN/'
    id_field = 'id'
    _fields = [
        f.StringField('description', display_name='Description'),
        f.StringField('info', display_name='Comments'),
        f.IntegerField('number', display_name='Number'),
        f.StringField('rir', display_name='RIR'),
    ]
    _views = {'all': ['number', 'rir', 'description', 'info'], 'brief': ['number', 'rir', 'description']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['number']])
        return l.strip()

    @property
    def devices(self):
        cls = getattr(pynetdot.models, 'Device')
        return cls.search(bgplocalas=self.id)

    @property
    def ipblocks(self):
        cls = getattr(pynetdot.models, 'Ipblock')
        return cls.search(asn=self.id)


class BaseAsset(n.Netdot):
    '''
    Assets represent network hardware (devices or modules). If an asset is
    installed, it will be associated with a device or devicemodule object.
    '''
    resource = 'Asset/'
    id_field = 'id'
    _fields = [
        f.StringField('custom_serial', display_name='Custom S/N'),
        f.DateField('date_purchased', display_name='Date Purchased'),
        f.StringField('description', display_name='Description'),
        f.StringField('info', display_name='Comments'),
        f.StringField('inventory_number', display_name='Inventory'),
        f.LinkField('maint_contract', display_name='Maint Contract', link_to='MaintContract'),
        f.DateField('maint_from', display_name='Maint Start'),
        f.DateField('maint_until', display_name='Maint End'),
        f.LinkField('physaddr', display_name='Base MAC', link_to='PhysAddr'),
        f.StringField('po_number', display_name='PO Number'),
        f.LinkField('product_id', display_name='Product', link_to='Product'),
        f.StringField('reserved_for', display_name='Reserved For'),
        f.StringField('serial_number', display_name='S/N'),
    ]
    _views = {'all': ['serial_number', 'custom_serial', 'inventory_number', 'physaddr', 'product_id', 'description', 'po_number', 'reserved_for', 'date_purchased', 'maint_contract', 'maint_from', 'maint_until', 'info'], 'brief': ['serial_number', 'physaddr', 'product_id', 'inventory_number', 'maint_from', 'maint_until', 'reserved_for']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['product_id', 'serial_number', 'physaddr']])
        return l.strip()

    @property
    def devices(self):
        cls = getattr(pynetdot.models, 'Device')
        return cls.search(asset_id=self.id)

    @property
    def device_modules(self):
        cls = getattr(pynetdot.models, 'DeviceModule')
        return cls.search(asset_id=self.id)


class BaseAudit(n.Netdot):
    '''
    Audit Table to record database operations made by users
    '''
    resource = 'Audit/'
    id_field = 'id'
    _fields = [
        f.StringField('fields', display_name='Fields'),
        f.StringField('label', display_name='Label'),
        f.IntegerField('object_id', display_name='Object ID'),
        f.StringField('operation', display_name='Operation'),
        f.StringField('tablename', display_name='Table'),
        f.DateTimeField('tstamp', display_name='Timestamp'),
        f.StringField('username', display_name='Username'),
        f.StringField('vals', display_name='Values'),
    ]
    _views = {'all': ['tstamp', 'username', 'tablename', 'label', 'object_id', 'operation', 'fields', 'vals'], 'brief': ['tstamp', 'username', 'tablename', 'label', 'operation']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['tstamp', 'username', 'label']])
        return l.strip()


class BaseAvailability(n.Netdot):
    '''
    A Time Period
    '''
    resource = 'Availability/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Time Period'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def page_notifications(self):
        cls = getattr(pynetdot.models, 'Contact')
        return cls.search(notify_email=self.id)

    @property
    def page_notifications(self):
        cls = getattr(pynetdot.models, 'Contact')
        return cls.search(notify_pager=self.id)

    @property
    def page_notifications(self):
        cls = getattr(pynetdot.models, 'Contact')
        return cls.search(notify_voice=self.id)

    @property
    def entities(self):
        cls = getattr(pynetdot.models, 'Entity')
        return cls.search(availability=self.id)

    @property
    def sites(self):
        cls = getattr(pynetdot.models, 'Site')
        return cls.search(availability=self.id)


class BaseBackboneCable(n.Netdot):
    '''
    A Backbone cable that interconnects two sites.  Backbone cables can have
    multiple strands.
    '''
    resource = 'BackboneCable/'
    id_field = 'id'
    _fields = [
        f.LinkField('end_closet', display_name='Destination Closet', link_to='Closet'),
        f.StringField('info', display_name='Comments'),
        f.DateField('installdate', display_name='Installed on'),
        f.StringField('length', display_name='Length'),
        f.StringField('name', display_name='Cable ID'),
        f.LinkField('owner', display_name='Owned by', link_to='Entity'),
        f.LinkField('start_closet', display_name='Origin Closet', link_to='Closet'),
        f.LinkField('type', display_name='Cable Type', link_to='CableType'),
    ]
    _views = {'all': ['name', 'type', 'owner', 'installdate', 'start_closet', 'end_closet', 'length', 'info'], 'brief': ['name', 'start_closet', 'end_closet']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def strands(self):
        cls = getattr(pynetdot.models, 'CableStrand')
        return cls.search(cable=self.id)


class BaseBGPPeering(n.Netdot):
    '''
    A BGP Peering
    '''
    resource = 'BGPPeering/'
    id_field = 'id'
    _fields = [
        f.StringField('authkey', display_name='Auth key'),
        f.StringField('bgppeeraddr', display_name='Peer Adress'),
        f.StringField('bgppeerid', display_name='Peer ID'),
        f.LinkField('contactlist', display_name='Contact List', link_to='ContactList'),
        f.LinkField('device', display_name='Device', link_to='Device'),
        f.LinkField('entity', display_name='Entity', link_to='Entity'),
        f.StringField('info', display_name='Comments'),
        f.DateTimeField('last_changed', display_name='Last Changed'),
        f.IntegerField('max_v4_prefixes', display_name='Max IPv4 Prefixes'),
        f.IntegerField('max_v6_prefixes', display_name='Max IPv6 Prefixes'),
        f.BoolField('monitored', display_name='Monitored?'),
        f.StringField('peer_group', display_name='Peer Group'),
        f.StringField('state', display_name='State'),
    ]
    _views = {'all': ['device', 'entity', 'bgppeerid', 'bgppeeraddr', 'state', 'last_changed', 'max_v4_prefixes', 'max_v6_prefixes', 'monitored', 'authkey', 'peer_group', 'contactlist', 'info'], 'brief': ['device', 'entity', 'bgppeeraddr']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['device', 'entity']])
        return l.strip()


class BaseCableStrand(n.Netdot):
    '''
    A single cable strand/pair
    '''
    resource = 'CableStrand/'
    id_field = 'id'
    _fields = [
        f.LinkField('cable', display_name='Cable ID', link_to='BackboneCable'),
        f.LinkField('circuit_id', display_name='Circuit', link_to='Circuit'),
        f.StringField('description', display_name='Description'),
        f.LinkField('fiber_type', display_name='', link_to='FiberType'),
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Strand ID'),
        f.IntegerField('number', display_name='Number'),
        f.LinkField('status', display_name='Status', link_to='StrandStatus'),
    ]
    _views = {'all': ['name', 'number', 'cable', 'status', 'fiber_type', 'circuit_id', 'description', 'info'], 'brief': ['name', 'cable', 'status']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def splices(self):
        cls = getattr(pynetdot.models, 'Splice')
        return cls.search(strand1=self.id)

    @property
    def splices2(self):
        cls = getattr(pynetdot.models, 'Splice')
        return cls.search(strand2=self.id)


class BaseCableType(n.Netdot):
    '''
    Types of Cables
    '''
    resource = 'CableType/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def backbonecables(self):
        cls = getattr(pynetdot.models, 'BackboneCable')
        return cls.search(type=self.id)

    @property
    def horizontalcables(self):
        cls = getattr(pynetdot.models, 'HorizontalCable')
        return cls.search(type=self.id)


class BaseCircuit(n.Netdot):
    '''
    A circuit can either be a WAN link provided by an external entity, or a
    set of [spliced] backbone cable strands terminated into two device
    interfaces
    '''
    resource = 'Circuit/'
    id_field = 'id'
    _fields = [
        f.StringField('cid', display_name='Circuit ID'),
        f.DateField('datetested', display_name='Date Tested'),
        f.StringField('info', display_name='Comments'),
        f.DateField('installdate', display_name='Installed on'),
        f.LinkField('linkid', display_name='Site Link', link_to='SiteLink'),
        f.StringField('loss', display_name='Loss'),
        f.StringField('speed', display_name='Speed'),
        f.LinkField('status', display_name='Status', link_to='CircuitStatus'),
        f.LinkField('type', display_name='Type', link_to='CircuitType'),
        f.LinkField('vendor', display_name='Provider', link_to='Entity'),
    ]
    _views = {'all': ['cid', 'linkid', 'status', 'type', 'speed', 'installdate', 'datetested', 'loss', 'vendor', 'info'], 'brief': ['cid', 'linkid', 'type', 'vendor', 'status']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['cid']])
        return l.strip()

    @property
    def strands(self):
        cls = getattr(pynetdot.models, 'CableStrand')
        return cls.search(circuit_id=self.id)

    @property
    def interfaces(self):
        cls = getattr(pynetdot.models, 'Interface')
        return cls.search(circuit=self.id)


class BaseCircuitStatus(n.Netdot):
    '''
    Circuit status
    '''
    resource = 'CircuitStatus/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Status'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def circuits(self):
        cls = getattr(pynetdot.models, 'Circuit')
        return cls.search(status=self.id)


class BaseCircuitType(n.Netdot):
    '''
    Circuit Type
    '''
    resource = 'CircuitType/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Type'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def circuits(self):
        cls = getattr(pynetdot.models, 'Circuit')
        return cls.search(type=self.id)


class BaseCloset(n.Netdot):
    '''
    A Communications Closet.  A Closet is different from a normal Room in two
    ways: a) Backbone Cables (inter and intra building) terminate in Closets.
    b) Horizontal Cables _start_ in Closets and _end_ in Rooms
    '''
    resource = 'Closet/'
    id_field = 'id'
    _fields = [
        f.StringField('access_key_type', display_name='Access Key Type'),
        f.BoolField('asbestos_tiles', display_name='Asbestos Tiles'),
        f.StringField('catv_taps', display_name='CableTV Taps'),
        f.BoolField('converted_patch_panels', display_name='Converted Patch Panels'),
        f.StringField('dimensions', display_name='Dimensions'),
        f.BoolField('ground_buss', display_name='Ground Buss'),
        f.StringField('hvac_type', display_name='HVAC Type'),
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
        f.StringField('ot_blocks', display_name='110 Blocks'),
        f.StringField('outlets', display_name='Outlets'),
        f.StringField('pair_count', display_name='Pair Count'),
        f.StringField('patch_panels', display_name='Patch Panels'),
        f.StringField('rack_type', display_name='Rack Type'),
        f.StringField('racks', display_name='Racks'),
        f.LinkField('room', display_name='Room', link_to='Room'),
        f.StringField('ru_avail', display_name='Rack Units Available'),
        f.StringField('shared_with', display_name='Shared With'),
        f.StringField('ss_blocks', display_name='66 Blocks'),
        f.StringField('work_needed', display_name='Work Needed'),
    ]
    _views = {'all': ['name', 'room', 'dimensions', 'racks', 'outlets', 'ru_avail', 'patch_panels', 'ot_blocks', 'ss_blocks', 'catv_taps', 'access_key_type', 'work_needed', 'shared_with', 'hvac_type', 'ground_buss', 'asbestos_tiles', 'rack_type', 'pair_count', 'converted_patch_panels', 'info'], 'brief': ['name', 'room']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name', 'room']])
        return l.strip()

    @property
    def backbones_end(self):
        cls = getattr(pynetdot.models, 'BackboneCable')
        return cls.search(end_closet=self.id)

    @property
    def backbones_start(self):
        cls = getattr(pynetdot.models, 'BackboneCable')
        return cls.search(start_closet=self.id)

    @property
    def horizontalcables(self):
        cls = getattr(pynetdot.models, 'HorizontalCable')
        return cls.search(closet=self.id)


class BaseContact(n.Netdot):
    '''
    A Contact object is basically a Role of a certain Person.  People can be
    associated with one or more resources (devices, services, etc) for which
    they could be contacted.  Each Contact object represents one of these
    roles.
    '''
    resource = 'Contact/'
    id_field = 'id'
    _fields = [
        f.LinkField('contactlist', display_name='Contact List', link_to='ContactList'),
        f.LinkField('contacttype', display_name='Type of Contact', link_to='ContactType'),
        f.IntegerField('escalation_level', display_name='Escalation Level'),
        f.StringField('info', display_name='Comments'),
        f.LinkField('notify_email', display_name='Email Notifications', link_to='Availability'),
        f.LinkField('notify_pager', display_name='Pager Notifications', link_to='Availability'),
        f.LinkField('notify_voice', display_name='Voice Notifications', link_to='Availability'),
        f.LinkField('person', display_name='Person', link_to='Person'),
    ]
    _views = {'all': ['person', 'contacttype', 'contactlist', 'notify_email', 'notify_pager', 'notify_voice', 'escalation_level', 'info'], 'brief': ['person', 'contacttype', 'contactlist']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['person', 'contacttype']])
        return l.strip()


class BaseContactList(n.Netdot):
    '''
    A list of contacts
    '''
    resource = 'ContactList/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name', 'info']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def peerings(self):
        cls = getattr(pynetdot.models, 'BGPPeering')
        return cls.search(contactlist=self.id)

    @property
    def contacts(self):
        cls = getattr(pynetdot.models, 'Contact')
        return cls.search(contactlist=self.id)

    @property
    def devices(self):
        cls = getattr(pynetdot.models, 'DeviceContacts')
        return cls.search(contactlist=self.id)

    @property
    def entities(self):
        cls = getattr(pynetdot.models, 'Entity')
        return cls.search(contactlist=self.id)

    @property
    def access_rights(self):
        cls = getattr(pynetdot.models, 'GroupRight')
        return cls.search(contactlist=self.id)

    @property
    def outlets(self):
        cls = getattr(pynetdot.models, 'HorizontalCable')
        return cls.search(contactlist=self.id)

    @property
    def interfaces(self):
        cls = getattr(pynetdot.models, 'Interface')
        return cls.search(contactlist=self.id)

    @property
    def services(self):
        cls = getattr(pynetdot.models, 'IpService')
        return cls.search(contactlist=self.id)

    @property
    def sites(self):
        cls = getattr(pynetdot.models, 'Site')
        return cls.search(contactlist=self.id)

    @property
    def zones(self):
        cls = getattr(pynetdot.models, 'Zone')
        return cls.search(contactlist=self.id)


class BaseContactType(n.Netdot):
    '''
    Type of contact
    '''
    resource = 'ContactType/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def contacts(self):
        cls = getattr(pynetdot.models, 'Contact')
        return cls.search(contacttype=self.id)


class BaseDevice(n.Netdot):
    '''
    A network device.  Particularly, Devices in Netdot are network
    infrastructure devices that network administrators care about for
    inventory, monitoring and management purposes.  Not to be confused with
    end nodes
    '''
    resource = 'Device/'
    id_field = 'id'
    _fields = [
        f.StringField('aliases', display_name='Aliases'),
        f.LinkField('asset_id', display_name='Asset', link_to='Asset'),
        f.BoolField('auto_dns', display_name='Auto DNS?'),
        f.StringField('bgpid', display_name='BGP ID'),
        f.LinkField('bgplocalas', display_name='BGP Local AS', link_to='ASN'),
        f.BoolField('canautoupdate', display_name='Auto Update?'),
        f.BoolField('collect_arp', display_name='Collect ARP?'),
        f.BoolField('collect_fwt', display_name='Collect FWT?'),
        f.BoolField('collect_stp', display_name='Collect STP Info?'),
        f.StringField('community', display_name='SNMP Community'),
        f.BoolField('customer_managed', display_name='Managed by Customer?'),
        f.DateTimeField('date_installed', display_name='First Discovered'),
        f.DateField('down_from', display_name='Down From'),
        f.DateField('down_until', display_name='Down Until'),
        f.IntegerField('extension', display_name='Extension'),
        f.LinkField('host_device', display_name='Host Device', link_to='Device'),
        f.StringField('info', display_name='Comments'),
        f.BoolField('ipforwarding', display_name='IP Forward?'),
        f.DateTimeField('last_arp', display_name='Last ARP'),
        f.DateTimeField('last_fwt', display_name='Last FWT'),
        f.DateTimeField('last_updated', display_name='Last Updated'),
        f.StringField('layers', display_name='OSI Layers'),
        f.BoolField('monitor_config', display_name='Monitor Config?'),
        f.StringField('monitor_config_group', display_name='Config Group'),
        f.BoolField('monitored', display_name='Monitored?'),
        f.IntegerField('monitoring_path_cost', display_name='Path Cost'),
        f.StringField('monitoring_template', display_name='Monitoring Template'),
        f.LinkField('monitorstatus', display_name='Monitored Status', link_to='MonitorStatus'),
        f.LinkField('name', display_name='Name', link_to='RR'),
        f.StringField('oobname', display_name='OOB Hostname #1'),
        f.StringField('oobname_2', display_name='OOB Hostname #2'),
        f.StringField('oobnumber', display_name='OOB Tel #1'),
        f.StringField('oobnumber_2', display_name='OOB Tel #2'),
        f.StringField('os', display_name='OS'),
        f.LinkField('owner', display_name='Owner', link_to='Entity'),
        f.StringField('power_outlet', display_name='Power #1'),
        f.StringField('power_outlet_2', display_name='Power #2'),
        f.StringField('rack', display_name='Rack'),
        f.LinkField('room', display_name='Room', link_to='Room'),
        f.LinkField('site', display_name='Site', link_to='Site'),
        f.StringField('snmp_authkey', display_name='AuthKey'),
        f.StringField('snmp_authprotocol', display_name='AuthProtocol'),
        f.BoolField('snmp_bulk', display_name='SNMP Bulk?'),
        f.IntegerField('snmp_conn_attempts', display_name='SNMP Failed Attempts'),
        f.BoolField('snmp_down', display_name='SNMP Down'),
        f.BoolField('snmp_managed', display_name='SNMP Managed?'),
        f.BoolField('snmp_polling', display_name='SNMP Polling?'),
        f.StringField('snmp_privkey', display_name='PrivKey'),
        f.StringField('snmp_privprotocol', display_name='PrivProtocol'),
        f.StringField('snmp_securitylevel', display_name='SecLevel'),
        f.StringField('snmp_securityname', display_name='SecName'),
        f.LinkField('snmp_target', display_name='SNMP Target Address', link_to='Ipblock'),
        f.IntegerField('snmp_version', display_name='SNMP Version'),
        f.BoolField('stp_enabled', display_name='STP Enabled?'),
        f.StringField('stp_mst_digest', display_name='MST Config Digest'),
        f.StringField('stp_mst_region', display_name='MST Region'),
        f.IntegerField('stp_mst_rev', display_name='MST Revision'),
        f.StringField('stp_type', display_name='STP Type'),
        f.StringField('sysdescription', display_name='System Description'),
        f.StringField('syslocation', display_name='System Location'),
        f.StringField('sysname', display_name='System Name'),
        f.LinkField('used_by', display_name='Used by', link_to='Entity'),
    ]
    _views = {'all': ['name', 'asset_id', 'aliases', 'snmp_target', 'sysname', 'sysdescription', 'syslocation', 'ipforwarding', 'layers', 'os', 'host_device', 'extension', 'bgplocalas', 'auto_dns', 'bgpid', 'oobname', 'oobname_2', 'oobnumber', 'oobnumber_2', 'power_outlet', 'power_outlet_2', 'owner', 'used_by', 'monitored', 'monitoring_path_cost', 'monitoring_template', 'monitorstatus', 'customer_managed', 'community', 'canautoupdate', 'site', 'monitor_config', 'monitor_config_group', 'snmp_managed', 'snmp_polling', 'collect_arp', 'last_arp', 'collect_fwt', 'collect_stp', 'last_fwt', 'snmp_bulk', 'snmp_version', 'snmp_securityname', 'snmp_authkey', 'snmp_authprotocol', 'snmp_privkey', 'snmp_privprotocol', 'snmp_securitylevel', 'snmp_conn_attempts', 'snmp_down', 'stp_enabled', 'stp_type', 'stp_mst_region', 'stp_mst_rev', 'stp_mst_digest', 'room', 'rack', 'last_updated', 'date_installed', 'down_from', 'down_until', 'info'], 'brief': ['name', 'asset_id', 'site', 'snmp_target']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def arp_caches(self):
        cls = getattr(pynetdot.models, 'ArpCache')
        return cls.search(device=self.id)

    @property
    def bgppeers(self):
        cls = getattr(pynetdot.models, 'BGPPeering')
        return cls.search(device=self.id)

    @property
    def hosted_devices(self):
        cls = getattr(pynetdot.models, 'Device')
        return cls.search(host_device=self.id)

    @property
    def attributes(self):
        cls = getattr(pynetdot.models, 'DeviceAttr')
        return cls.search(device=self.id)

    @property
    def modules(self):
        cls = getattr(pynetdot.models, 'DeviceModule')
        return cls.search(device=self.id)

    @property
    def contacts(self):
        cls = getattr(pynetdot.models, 'DeviceContacts')
        return cls.search(device=self.id)

    @property
    def forwarding_tables(self):
        cls = getattr(pynetdot.models, 'FWTable')
        return cls.search(device=self.id)

    @property
    def interfaces(self):
        cls = getattr(pynetdot.models, 'Interface')
        return cls.search(device=self.id)

    @property
    def stp_instances(self):
        cls = getattr(pynetdot.models, 'STPInstance')
        return cls.search(device=self.id)


class BaseDeviceAttr(n.Netdot):
    '''
    A Device Attribute
    '''
    resource = 'DeviceAttr/'
    id_field = 'id'
    _fields = [
        f.LinkField('device', display_name='Device', link_to='Device'),
        f.LinkField('name', display_name='Name', link_to='DeviceAttrName'),
        f.StringField('value', display_name='Value'),
    ]
    _views = {'all': ['name', 'value', 'device'], 'brief': ['name', 'value', 'device']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name', 'value', 'device']])
        return l.strip()


class BaseDeviceAttrName(n.Netdot):
    '''
    A Device Attributes Name
    '''
    resource = 'DeviceAttrName/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def attributes(self):
        cls = getattr(pynetdot.models, 'DeviceAttr')
        return cls.search(name=self.id)


class BaseDeviceContacts(n.Netdot):
    '''
    Device to Contactlist join table
    '''
    resource = 'DeviceContacts/'
    id_field = 'id'
    _fields = [
        f.LinkField('contactlist', display_name='Contact List', link_to='ContactList'),
        f.LinkField('device', display_name='Device', link_to='Device'),
    ]
    _views = {'all': ['device', 'contactlist'], 'brief': ['device', 'contactlist']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['contactlist']])
        return l.strip()


class BaseDeviceModule(n.Netdot):
    '''
    A Device Physical Entity
    '''
    resource = 'DeviceModule/'
    id_field = 'id'
    _fields = [
        f.LinkField('asset_id', display_name='Asset', link_to='Asset'),
        f.StringField('class', display_name='Class'),
        f.IntegerField('contained_in', display_name='Contained In'),
        f.DateTimeField('date_installed', display_name='First Discovered'),
        f.StringField('description', display_name='Description'),
        f.LinkField('device', display_name='Device', link_to='Device'),
        f.BoolField('fru', display_name='FRU?'),
        f.StringField('fw_rev', display_name='Firmware Revision'),
        f.StringField('hw_rev', display_name='Hardware Revision'),
        f.DateTimeField('last_updated', display_name='Last Updated'),
        f.StringField('model', display_name='Model'),
        f.StringField('name', display_name='Name'),
        f.IntegerField('number', display_name='Number'),
        f.IntegerField('pos', display_name='Position'),
        f.StringField('sw_rev', display_name='Software Revision'),
        f.StringField('type', display_name='Type'),
    ]
    _views = {'all': ['device', 'contained_in', 'number', 'pos', 'name', 'type', 'class', 'description', 'model', 'hw_rev', 'fw_rev', 'sw_rev', 'fru', 'asset_id', 'date_installed', 'last_updated'], 'brief': ['number', 'name', 'class', 'model', 'description', 'asset_id']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name', 'model', 'device']])
        return l.strip()


class BaseDhcpAttr(n.Netdot):
    '''
    A DHCP Attribute or Parameter
    '''
    resource = 'DhcpAttr/'
    id_field = 'id'
    _fields = [
        f.LinkField('name', display_name='Name', link_to='DhcpAttrName'),
        f.LinkField('scope', display_name='Scope', link_to='DhcpScope'),
        f.StringField('value', display_name='Value'),
    ]
    _views = {'all': ['name', 'value', 'scope'], 'brief': ['name', 'value', 'scope']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name', 'value']])
        return l.strip()


class BaseDhcpAttrName(n.Netdot):
    '''
    A DHCP Attributes Name
    '''
    resource = 'DhcpAttrName/'
    id_field = 'id'
    _fields = [
        f.IntegerField('code', display_name='Code'),
        f.StringField('format', display_name='Format'),
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
    ]
    _views = {'all': ['name', 'code', 'format', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def attributes(self):
        cls = getattr(pynetdot.models, 'DhcpAttr')
        return cls.search(name=self.id)


class BaseDhcpScope(n.Netdot):
    '''
    A DHCP Scope
    '''
    resource = 'DhcpScope/'
    id_field = 'id'
    _fields = [
        f.BoolField('active', display_name='Active?'),
        f.LinkField('container', display_name='Container Scope', link_to='DhcpScope'),
        f.StringField('duid', display_name='DUID'),
        f.BoolField('enable_failover', display_name='Enable Failover?'),
        f.StringField('export_file', display_name='Export File'),
        f.StringField('failover_peer', display_name='Failover Peer'),
        f.LinkField('ipblock', display_name='IP block', link_to='Ipblock'),
        f.StringField('name', display_name='Name'),
        f.LinkField('physaddr', display_name='Ethernet', link_to='PhysAddr'),
        f.StringField('text', display_name='Include Text'),
        f.LinkField('type', display_name='Type', link_to='DhcpScopeType'),
        f.IntegerField('version', display_name='Version (4|6)'),
    ]
    _views = {'subnet': ['name', 'type', 'active', 'container', 'ipblock', 'enable_failover', 'failover_peer', 'text'], 'all': ['name', 'type', 'version', 'container', 'active', 'ipblock', 'physaddr', 'duid', 'text', 'enable_failover', 'failover_peer', 'export_file'], 'group': ['name', 'type', 'active', 'container', 'text'], 'global': ['name', 'type', 'version', 'active', 'enable_failover', 'failover_peer', 'export_file', 'text'], 'brief': ['name', 'type'], 'subclass': ['name', 'type', 'active', 'container', 'text'], 'host': ['name', 'type', 'active', 'container', 'ipblock', 'duid', 'physaddr', 'text'], 'shared-network': ['name', 'type', 'active', 'container', 'text'], 'class': ['name', 'type', 'active', 'container', 'text'], 'pool': ['name', 'type', 'active', 'container', 'text']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['type', 'name']])
        return l.strip()

    @property
    def attributes(self):
        cls = getattr(pynetdot.models, 'DhcpAttr')
        return cls.search(scope=self.id)

    @property
    def contained_scopes(self):
        cls = getattr(pynetdot.models, 'DhcpScope')
        return cls.search(container=self.id)

    @property
    def templates(self):
        cls = getattr(pynetdot.models, 'DhcpScopeUse')
        return cls.search(scope=self.id)

    @property
    def derived_scopes(self):
        cls = getattr(pynetdot.models, 'DhcpScopeUse')
        return cls.search(template=self.id)


class BaseDhcpScopeType(n.Netdot):
    '''
    A DHCP Scope Type
    '''
    resource = 'DhcpScopeType/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def scopes(self):
        cls = getattr(pynetdot.models, 'DhcpScope')
        return cls.search(type=self.id)


class BaseDhcpScopeUse(n.Netdot):
    '''
    Relationship between a scopes and scope templates
    '''
    resource = 'DhcpScopeUse/'
    id_field = 'id'
    _fields = [
        f.LinkField('scope', display_name='Scope', link_to='DhcpScope'),
        f.LinkField('template', display_name='Template', link_to='DhcpScope'),
    ]
    _views = {'all': ['scope', 'template'], 'brief': ['scope', 'template']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['scope', 'template']])
        return l.strip()


class BaseEntity(n.Netdot):
    '''
    An organization related to the network in some way
    '''
    resource = 'Entity/'
    id_field = 'id'
    _fields = [
        f.StringField('acctnumber', display_name='Account Number'),
        f.StringField('aliases', display_name='Aliases'),
        f.StringField('asname', display_name='AS Name'),
        f.IntegerField('asnumber', display_name='AS Number'),
        f.LinkField('availability', display_name='Availability', link_to='Availability'),
        f.StringField('config_type', display_name='Config Type'),
        f.LinkField('contactlist', display_name='Contact List', link_to='ContactList'),
        f.StringField('info', display_name='Comments'),
        f.StringField('maint_contract', display_name='Maintenance Contract'),
        f.StringField('name', display_name='Name'),
        f.StringField('oid', display_name='Enterprise OID'),
        f.StringField('short_name', display_name='Short Name'),
    ]
    _views = {'peer': ['name', 'aliases', 'short_name', 'type', 'availability', 'contactlist', 'asname', 'asnumber', 'info'], 'all': ['name', 'aliases', 'short_name', 'availability', 'contactlist', 'acctnumber', 'maint_contract', 'asname', 'asnumber', 'oid', 'config_type', 'info'], 'provider': ['name', 'aliases', 'short_name', 'type', 'availability', 'contactlist', 'asname', 'asnumber', 'info'], 'brief': ['name', 'short_name'], 'manufacturer': ['name', 'aliases', 'short_name', 'type', 'contactlist', 'oid', 'config_type', 'info']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def bgppeers(self):
        cls = getattr(pynetdot.models, 'BGPPeering')
        return cls.search(entity=self.id)

    @property
    def cables(self):
        cls = getattr(pynetdot.models, 'BackboneCable')
        return cls.search(owner=self.id)

    @property
    def circuits(self):
        cls = getattr(pynetdot.models, 'Circuit')
        return cls.search(vendor=self.id)

    @property
    def links(self):
        cls = getattr(pynetdot.models, 'SiteLink')
        return cls.search(entity=self.id)

    @property
    def owned_devices(self):
        cls = getattr(pynetdot.models, 'Device')
        return cls.search(owner=self.id)

    @property
    def used_devices(self):
        cls = getattr(pynetdot.models, 'Device')
        return cls.search(used_by=self.id)

    @property
    def roles(self):
        cls = getattr(pynetdot.models, 'EntityRole')
        return cls.search(entity=self.id)

    @property
    def sites(self):
        cls = getattr(pynetdot.models, 'EntitySite')
        return cls.search(entity=self.id)

    @property
    def owned_blocks(self):
        cls = getattr(pynetdot.models, 'Ipblock')
        return cls.search(owner=self.id)

    @property
    def used_blocks(self):
        cls = getattr(pynetdot.models, 'Ipblock')
        return cls.search(used_by=self.id)

    @property
    def maintenance_contracts(self):
        cls = getattr(pynetdot.models, 'MaintContract')
        return cls.search(provider=self.id)

    @property
    def employees(self):
        cls = getattr(pynetdot.models, 'Person')
        return cls.search(entity=self.id)

    @property
    def products(self):
        cls = getattr(pynetdot.models, 'Product')
        return cls.search(manufacturer=self.id)


class BaseEntityRole(n.Netdot):
    '''
    An Entity might play different roles.  For example, the same Entity can be
    both a Customer and a Peer.
    '''
    resource = 'EntityRole/'
    id_field = 'id'
    _fields = [
        f.LinkField('entity', display_name='Entity', link_to='Entity'),
        f.LinkField('type', display_name='Type', link_to='EntityType'),
    ]
    _views = {'all': ['entity', 'type'], 'brief': ['entity', 'type']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['entity', 'type']])
        return l.strip()


class BaseEntitySite(n.Netdot):
    '''
    Entity to Site join table
    '''
    resource = 'EntitySite/'
    id_field = 'id'
    _fields = [
        f.LinkField('entity', display_name='Entity', link_to='Entity'),
        f.LinkField('site', display_name='Site', link_to='Site'),
    ]
    _views = {'all': ['entity', 'site'], 'brief': ['entity', 'site']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['entity', 'site']])
        return l.strip()


class BaseEntityType(n.Netdot):
    '''
    Types of Entities
    '''
    resource = 'EntityType/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def roles(self):
        cls = getattr(pynetdot.models, 'EntityRole')
        return cls.search(type=self.id)


class BaseFiberType(n.Netdot):
    '''
    Types of Fiber
    '''
    resource = 'FiberType/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def strands(self):
        cls = getattr(pynetdot.models, 'CableStrand')
        return cls.search(fiber_type=self.id)


class BaseFloor(n.Netdot):
    '''
    Floor Table
    '''
    resource = 'Floor/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('level', display_name='Level'),
        f.LinkField('site', display_name='Site', link_to='Site'),
    ]
    _views = {'all': ['level', 'site', 'info'], 'brief': ['level', 'site']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['level', 'site']])
        return l.strip()

    @property
    def rooms(self):
        cls = getattr(pynetdot.models, 'Room')
        return cls.search(floor=self.id)


class BaseFWTable(n.Netdot):
    '''
    Bridge Forwarding Table.  One of these is created every time a Device is
    queried.  Entries in these tables contain physical addresses and the ports
    where they have been seen.
    '''
    resource = 'FWTable/'
    id_field = 'id'
    _fields = [
        f.LinkField('device', display_name='Device', link_to='Device'),
        f.DateTimeField('tstamp', display_name='Timestamp'),
    ]
    _views = {'all': ['tstamp', 'device'], 'brief': ['tstamp', 'device']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['tstamp', 'device']])
        return l.strip()

    @property
    def entries(self):
        cls = getattr(pynetdot.models, 'FWTableEntry')
        return cls.search(fwtable=self.id)


class BaseFWTableEntry(n.Netdot):
    '''
    Bridge Forwarding Table entry
    '''
    resource = 'FWTableEntry/'
    id_field = 'id'
    _fields = [
        f.LinkField('fwtable', display_name='Table', link_to='FWTable'),
        f.LinkField('interface', display_name='Interface', link_to='Interface'),
        f.LinkField('physaddr', display_name='Physical Address', link_to='PhysAddr'),
    ]
    _views = {'all': ['interface', 'physaddr', 'fwtable'], 'brief': ['interface', 'physaddr']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['interface', 'physaddr']])
        return l.strip()


class BaseGroupRight(n.Netdot):
    '''
    Join between a ContactList and its Access Rights
    '''
    resource = 'GroupRight/'
    id_field = 'id'
    _fields = [
        f.LinkField('accessright', display_name='Access Right', link_to='AccessRight'),
        f.LinkField('contactlist', display_name='Contact List', link_to='ContactList'),
    ]
    _views = {'all': ['contactlist', 'accessright'], 'brief': ['contactlist', 'accessright']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['contactlist', 'accessright']])
        return l.strip()


class BaseHorizontalCable(n.Netdot):
    '''
    Horizontal Cable
    '''
    resource = 'HorizontalCable/'
    id_field = 'id'
    _fields = [
        f.StringField('account', display_name='Account'),
        f.LinkField('closet', display_name='Closet', link_to='Closet'),
        f.LinkField('contactlist', display_name='Contact List', link_to='ContactList'),
        f.DateField('datetested', display_name='Date Tested'),
        f.StringField('faceplateid', display_name='Faceplate ID'),
        f.StringField('info', display_name='Comments'),
        f.DateField('installdate', display_name='Date Installed'),
        f.StringField('jackid', display_name='Jack ID'),
        f.StringField('length', display_name='Length'),
        f.LinkField('room', display_name='Room', link_to='Room'),
        f.BoolField('testpassed', display_name='Passed Test?'),
        f.LinkField('type', display_name='Type', link_to='CableType'),
    ]
    _views = {'all': ['jackid', 'faceplateid', 'type', 'datetested', 'testpassed', 'installdate', 'length', 'closet', 'room', 'account', 'contactlist', 'info'], 'brief': ['jackid', 'closet', 'room']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['jackid']])
        return l.strip()

    @property
    def interfaces(self):
        cls = getattr(pynetdot.models, 'Interface')
        return cls.search(jack=self.id)


class BaseHostAudit(n.Netdot):
    '''
    DNS and DHCP changes
    '''
    resource = 'HostAudit/'
    id_field = 'id'
    _fields = [
        f.BoolField('pending', display_name=''),
        f.StringField('scope', display_name='DHCP Scope'),
        f.DateTimeField('tstamp', display_name='Timestamp'),
        f.StringField('zone', display_name='Zone'),
    ]
    _views = {'all': ['tstamp', 'zone', 'scope', 'pending'], 'brief': ['tstamp', 'zone', 'scope', 'pending']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['zone']])
        return l.strip()


class BaseInterface(n.Netdot):
    '''
    An interface associated with a device
    '''
    resource = 'Interface/'
    id_field = 'id'
    _fields = [
        f.StringField('admin_duplex', display_name='Admin Duplex'),
        f.StringField('admin_status', display_name='Admin Status'),
        f.BoolField('auto_dns', display_name='Auto DNS?'),
        f.BoolField('bpdu_filter_enabled', display_name='BPDU Filter?'),
        f.BoolField('bpdu_guard_enabled', display_name='BPDU Guard?'),
        f.LinkField('circuit', display_name='Circuit', link_to='Circuit'),
        f.LinkField('contactlist', display_name='Contact List', link_to='ContactList'),
        f.StringField('description', display_name='Description'),
        f.LinkField('device', display_name='Device', link_to='Device'),
        f.StringField('dlci', display_name='DLCI'),
        f.StringField('doc_status', display_name='Doc Status'),
        f.DateField('down_from', display_name='Down From'),
        f.DateField('down_until', display_name='Down Until'),
        f.StringField('dp_remote_id', display_name='DP Remote ID'),
        f.StringField('dp_remote_ip', display_name='DP Remote IP'),
        f.StringField('dp_remote_port', display_name='DP Remote Port'),
        f.StringField('dp_remote_type', display_name='DP Remote Type'),
        f.BoolField('ignore_ip', display_name='Ignore IP?'),
        f.StringField('info', display_name='Comments'),
        f.LinkField('jack', display_name='Jack', link_to='HorizontalCable'),
        f.StringField('jack_char', display_name='Jack(char)'),
        f.BoolField('loop_guard_enabled', display_name='Loop Guard?'),
        f.BoolField('monitored', display_name='Monitored?'),
        f.LinkField('monitorstatus', display_name='Monitored Status', link_to='MonitorStatus'),
        f.StringField('name', display_name='Name'),
        f.LinkField('neighbor', display_name='Neighbor', link_to='Interface'),
        f.BoolField('neighbor_fixed', display_name='Neighbor Fixed?'),
        f.IntegerField('neighbor_missed', display_name='Neighbor Missed'),
        f.StringField('number', display_name='Number'),
        f.StringField('oper_duplex', display_name='Oper Duplex'),
        f.StringField('oper_status', display_name='Oper Status'),
        f.BoolField('overwrite_descr', display_name='Overwrite Description?'),
        f.LinkField('physaddr', display_name='Physical (MAC) Address', link_to='PhysAddr'),
        f.StringField('room_char', display_name='Room(char)'),
        f.BoolField('root_guard_enabled', display_name='Root Guard?'),
        f.BoolField('snmp_managed', display_name='SNMP-Managed?'),
        f.IntegerField('speed', display_name='Speed'),
        f.StringField('stp_id', display_name='STP Port ID'),
        f.StringField('type', display_name='Type'),
    ]
    _views = {'all': ['number', 'name', 'device', 'doc_status', 'jack', 'jack_char', 'room_char', 'circuit', 'dlci', 'description', 'overwrite_descr', 'type', 'speed', 'admin_duplex', 'oper_duplex', 'admin_status', 'auto_dns', 'oper_status', 'monitored', 'monitorstatus', 'snmp_managed', 'physaddr', 'neighbor', 'neighbor_fixed', 'neighbor_missed', 'stp_id', 'bpdu_filter_enabled', 'bpdu_guard_enabled', 'loop_guard_enabled', 'root_guard_enabled', 'ignore_ip', 'dp_remote_id', 'dp_remote_ip', 'dp_remote_port', 'dp_remote_type', 'down_from', 'down_until', 'contactlist', 'info'], 'brief': ['number', 'name', 'device', 'jack', 'description', 'neighbor']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name', 'device']])
        return l.strip()

    @property
    def arp_entries(self):
        cls = getattr(pynetdot.models, 'ArpCacheEntry')
        return cls.search(interface=self.id)

    @property
    def fwt_entries(self):
        cls = getattr(pynetdot.models, 'FWTableEntry')
        return cls.search(interface=self.id)

    @property
    def neighbors(self):
        cls = getattr(pynetdot.models, 'Interface')
        return cls.search(neighbor=self.id)

    @property
    def vlans(self):
        cls = getattr(pynetdot.models, 'InterfaceVlan')
        return cls.search(interface=self.id)

    @property
    def ips(self):
        cls = getattr(pynetdot.models, 'Ipblock')
        return cls.search(interface=self.id)


class BaseInterfaceVlan(n.Netdot):
    '''
    Interface to VLAN join table
    '''
    resource = 'InterfaceVlan/'
    id_field = 'id'
    _fields = [
        f.LinkField('interface', display_name='Interface', link_to='Interface'),
        f.StringField('stp_des_bridge', display_name='STP Des. Bridge'),
        f.StringField('stp_des_port', display_name='STP Des. Port'),
        f.LinkField('stp_instance', display_name='STP Instance', link_to='STPInstance'),
        f.StringField('stp_state', display_name='STP State'),
        f.LinkField('vlan', display_name='Vlan', link_to='Vlan'),
    ]
    _views = {'all': ['interface', 'vlan', 'stp_instance', 'stp_des_bridge', 'stp_des_port', 'stp_state'], 'brief': ['interface', 'vlan', 'stp_instance', 'stp_des_bridge', 'stp_des_port', 'stp_state']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['interface', 'vlan']])
        return l.strip()


class BaseIpblock(n.Netdot):
    '''
    An IP (v4 or v6) CIDR block, which can represent both individual addresses
    and blocks of addresses (subnets, etc).
    '''
    resource = 'Ipblock/'
    id_field = 'id'
    _fields = [
        f.StringField('address', display_name='Address'),
        f.LinkField('asn', display_name='ASN', link_to='ASN'),
        f.StringField('description', display_name='Description'),
        f.DateTimeField('first_seen', display_name='First Seen'),
        f.StringField('info', display_name='Comments'),
        f.LinkField('interface', display_name='Interface', link_to='Interface'),
        f.DateTimeField('last_seen', display_name='Last Seen'),
        f.BoolField('monitored', display_name='Monitored?'),
        f.LinkField('owner', display_name='Owner', link_to='Entity'),
        f.LinkField('parent', display_name='Parent', link_to='Ipblock'),
        f.IntegerField('prefix', display_name='Prefix Length'),
        f.StringField('rir', display_name='RIR'),
        f.LinkField('status', display_name='Status', link_to='IpblockStatus'),
        f.BoolField('use_network_broadcast', display_name='Use Network/Broadcast?'),
        f.LinkField('used_by', display_name='Used by', link_to='Entity'),
        f.IntegerField('version', display_name='Version(4/6)'),
        f.LinkField('vlan', display_name='Vlan', link_to='Vlan'),
    ]
    _views = {'address_brief': ['address', 'status', 'used_by', 'description', 'last_seen'], 'all': ['address', 'prefix', 'version', 'parent', 'interface', 'vlan', 'status', 'monitored', 'owner', 'used_by', 'rir', 'asn', 'description', 'first_seen', 'last_seen', 'use_network_broadcast', 'info'], 'brief': ['address', 'prefix', 'status', 'used_by', 'description', 'last_seen'], 'subnet_brief': ['address', 'prefix', 'status', 'vlan', 'used_by', 'description'], 'container_brief': ['address', 'prefix', 'status', 'owner', 'used_by', 'rir', 'asn', 'description']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['address', 'prefix']])
        return l.strip()

    @property
    def arp_entries(self):
        cls = getattr(pynetdot.models, 'ArpCacheEntry')
        return cls.search(ipaddr=self.id)

    @property
    def snmp_devices(self):
        cls = getattr(pynetdot.models, 'Device')
        return cls.search(snmp_target=self.id)

    @property
    def dhcp_scopes(self):
        cls = getattr(pynetdot.models, 'DhcpScope')
        return cls.search(ipblock=self.id)

    @property
    def services(self):
        cls = getattr(pynetdot.models, 'IpService')
        return cls.search(ip=self.id)

    @property
    def children(self):
        cls = getattr(pynetdot.models, 'Ipblock')
        return cls.search(parent=self.id)

    @property
    def attributes(self):
        cls = getattr(pynetdot.models, 'IpblockAttr')
        return cls.search(ipblock=self.id)

    @property
    def a_records(self):
        cls = getattr(pynetdot.models, 'RRADDR')
        return cls.search(ipblock=self.id)

    @property
    def ptr_records(self):
        cls = getattr(pynetdot.models, 'RRPTR')
        return cls.search(ipblock=self.id)

    @property
    def sites(self):
        cls = getattr(pynetdot.models, 'SiteSubnet')
        return cls.search(subnet=self.id)

    @property
    def zones(self):
        cls = getattr(pynetdot.models, 'SubnetZone')
        return cls.search(subnet=self.id)


class BaseIpblockAttr(n.Netdot):
    '''
    An Ipblock Attribute
    '''
    resource = 'IpblockAttr/'
    id_field = 'id'
    _fields = [
        f.LinkField('ipblock', display_name='Ipblock', link_to='Ipblock'),
        f.LinkField('name', display_name='Name', link_to='IpblockAttrName'),
        f.StringField('value', display_name='Value'),
    ]
    _views = {'all': ['name', 'value', 'ipblock'], 'brief': ['name', 'value', 'ipblock']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name', 'value', 'ipblock']])
        return l.strip()


class BaseIpblockAttrName(n.Netdot):
    '''
    An Ipblock Attributes Name
    '''
    resource = 'IpblockAttrName/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def attributes(self):
        cls = getattr(pynetdot.models, 'IpblockAttr')
        return cls.search(name=self.id)


class BaseIpblockStatus(n.Netdot):
    '''
    IP block status
    '''
    resource = 'IpblockStatus/'
    id_field = 'id'
    _fields = [
        f.StringField('name', display_name=''),
    ]
    _views = {'all': ['name'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def ipblocks(self):
        cls = getattr(pynetdot.models, 'Ipblock')
        return cls.search(status=self.id)


class BaseIpService(n.Netdot):
    '''
    A relationship between an IP address and a running Internet service
    '''
    resource = 'IpService/'
    id_field = 'id'
    _fields = [
        f.LinkField('contactlist', display_name='', link_to='ContactList'),
        f.LinkField('ip', display_name='', link_to='Ipblock'),
        f.BoolField('monitored', display_name=''),
        f.LinkField('monitorstatus', display_name='', link_to='MonitorStatus'),
        f.LinkField('service', display_name='', link_to='Service'),
    ]
    _views = {'all': ['ip', 'service', 'monitored', 'monitorstatus', 'contactlist'], 'brief': ['ip', 'service']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['ip', 'service']])
        return l.strip()


class BaseMaintContract(n.Netdot):
    '''
    Device Maintenance Contract
    '''
    resource = 'MaintContract/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('number', display_name='Number'),
        f.LinkField('provider', display_name='Provider', link_to='Entity'),
    ]
    _views = {'all': ['number', 'provider', 'info'], 'brief': ['number']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['provider', 'number']])
        return l.strip()

    @property
    def assets(self):
        cls = getattr(pynetdot.models, 'Asset')
        return cls.search(maint_contract=self.id)


class BaseMonitorStatus(n.Netdot):
    '''
    Status information for what is monitored
    '''
    resource = 'MonitorStatus/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Status'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def devices(self):
        cls = getattr(pynetdot.models, 'Device')
        return cls.search(monitorstatus=self.id)

    @property
    def interfaces(self):
        cls = getattr(pynetdot.models, 'Interface')
        return cls.search(monitorstatus=self.id)

    @property
    def ipservices(self):
        cls = getattr(pynetdot.models, 'IpService')
        return cls.search(monitorstatus=self.id)


class BaseOUI(n.Netdot):
    '''
    Organizationally Unique Identifier
    '''
    resource = 'OUI/'
    id_field = 'id'
    _fields = [
        f.StringField('oui', display_name='OUI'),
        f.StringField('vendor', display_name='Vendor'),
    ]
    _views = {'all': ['oui', 'vendor'], 'brief': ['oui', 'vendor']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['oui', 'vendor']])
        return l.strip()


class BasePerson(n.Netdot):
    '''
    Information about an individual
    '''
    resource = 'Person/'
    id_field = 'id'
    _fields = [
        f.StringField('aliases', display_name='Aliases'),
        f.StringField('cell', display_name='Cell Phone'),
        f.StringField('email', display_name='Email'),
        f.StringField('emailpager', display_name='Pager Email'),
        f.LinkField('entity', display_name='Employer', link_to='Entity'),
        f.IntegerField('extension', display_name='Work Phone Extension'),
        f.StringField('fax', display_name='Fax'),
        f.StringField('firstname', display_name='First Name'),
        f.StringField('home', display_name='Home Phone'),
        f.StringField('info', display_name='Comments'),
        f.StringField('lastname', display_name='Last Name'),
        f.LinkField('location', display_name='Site', link_to='Site'),
        f.StringField('office', display_name='Work Phone'),
        f.StringField('pager', display_name='Pager'),
        f.StringField('password', display_name='Password'),
        f.StringField('position', display_name='Position'),
        f.LinkField('room', display_name='Room', link_to='Room'),
        f.LinkField('user_type', display_name='User Type', link_to='UserType'),
        f.StringField('username', display_name='Username'),
    ]
    _views = {'all': ['firstname', 'lastname', 'aliases', 'username', 'password', 'user_type', 'position', 'entity', 'location', 'room', 'email', 'office', 'extension', 'cell', 'home', 'pager', 'emailpager', 'fax', 'info'], 'brief': ['firstname', 'lastname', 'office', 'entity']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['lastname', 'firstname']])
        return l.strip()

    @property
    def roles(self):
        cls = getattr(pynetdot.models, 'Contact')
        return cls.search(person=self.id)


class BasePhysAddr(n.Netdot):
    '''
    A physical or MAC address
    '''
    resource = 'PhysAddr/'
    id_field = 'id'
    _fields = [
        f.StringField('address', display_name='Address'),
        f.DateTimeField('first_seen', display_name='First Seen'),
        f.DateTimeField('last_seen', display_name='Last Seen'),
        f.BoolField('static', display_name='Static?'),
    ]
    _views = {'all': ['address', 'static', 'first_seen', 'last_seen'], 'brief': ['address', 'static', 'first_seen', 'last_seen']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['address']])
        return l.strip()

    @property
    def arp_entries(self):
        cls = getattr(pynetdot.models, 'ArpCacheEntry')
        return cls.search(physaddr=self.id)

    @property
    def assets(self):
        cls = getattr(pynetdot.models, 'Asset')
        return cls.search(physaddr=self.id)

    @property
    def dhcp_hosts(self):
        cls = getattr(pynetdot.models, 'DhcpScope')
        return cls.search(physaddr=self.id)

    @property
    def fwt_entries(self):
        cls = getattr(pynetdot.models, 'FWTableEntry')
        return cls.search(physaddr=self.id)

    @property
    def interfaces(self):
        cls = getattr(pynetdot.models, 'Interface')
        return cls.search(physaddr=self.id)

    @property
    def attributes(self):
        cls = getattr(pynetdot.models, 'PhysAddrAttr')
        return cls.search(physaddr=self.id)


class BasePhysAddrAttr(n.Netdot):
    '''
    Custom attributes can be assigned to physical (MAC) addresses
    '''
    resource = 'PhysAddrAttr/'
    id_field = 'id'
    _fields = [
        f.LinkField('name', display_name='Name', link_to='PhysAddrAttrName'),
        f.LinkField('physaddr', display_name='Physical Address', link_to='PhysAddr'),
        f.StringField('value', display_name='Value'),
    ]
    _views = {'all': ['name', 'value', 'physaddr'], 'brief': ['name', 'value', 'physaddr']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name', 'value', 'physaddr']])
        return l.strip()


class BasePhysAddrAttrName(n.Netdot):
    '''
    Custom attribute name for physical (MAC) addresses
    '''
    resource = 'PhysAddrAttrName/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def attributes(self):
        cls = getattr(pynetdot.models, 'PhysAddrAttr')
        return cls.search(name=self.id)


class BaseProduct(n.Netdot):
    '''
    Product Names
    '''
    resource = 'Product/'
    id_field = 'id'
    _fields = [
        f.StringField('config_type', display_name='Config Type'),
        f.StringField('description', display_name='Description'),
        f.StringField('info', display_name='Comments'),
        f.StringField('latest_os', display_name='Recommended OS'),
        f.LinkField('manufacturer', display_name='Manufacturer', link_to='Entity'),
        f.StringField('name', display_name='Name'),
        f.StringField('part_number', display_name='Part Number'),
        f.StringField('sysobjectid', display_name='System ID'),
        f.LinkField('type', display_name='Type', link_to='ProductType'),
    ]
    _views = {'all': ['name', 'type', 'description', 'sysobjectid', 'manufacturer', 'config_type', 'part_number', 'latest_os', 'info'], 'brief': ['name', 'type', 'description', 'manufacturer']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['manufacturer', 'name']])
        return l.strip()

    @property
    def assets(self):
        cls = getattr(pynetdot.models, 'Asset')
        return cls.search(product_id=self.id)


class BaseProductType(n.Netdot):
    '''
    Types of network devices
    '''
    resource = 'ProductType/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def products(self):
        cls = getattr(pynetdot.models, 'Product')
        return cls.search(type=self.id)


class BaseRoom(n.Netdot):
    '''
    Room
    '''
    resource = 'Room/'
    id_field = 'id'
    _fields = [
        f.LinkField('floor', display_name='Floor', link_to='Floor'),
        f.StringField('name', display_name='Number'),
    ]
    _views = {'all': ['name', 'floor'], 'brief': ['name', 'floor']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['floor', 'name']])
        return l.strip()

    @property
    def closets(self):
        cls = getattr(pynetdot.models, 'Closet')
        return cls.search(room=self.id)

    @property
    def devices(self):
        cls = getattr(pynetdot.models, 'Device')
        return cls.search(room=self.id)

    @property
    def jacks(self):
        cls = getattr(pynetdot.models, 'HorizontalCable')
        return cls.search(room=self.id)

    @property
    def people(self):
        cls = getattr(pynetdot.models, 'Person')
        return cls.search(room=self.id)


class BaseRR(n.Netdot):
    '''
    DNS Resource Record. Also known as the "owner", this object in Netdot
    groups all the records with the same name.
    '''
    resource = 'RR/'
    id_field = 'id'
    _fields = [
        f.BoolField('active', display_name='Active?'),
        f.BoolField('auto_update', display_name='Auto Update?'),
        f.DateTimeField('created', display_name='Created'),
        f.DateField('expiration', display_name='Expiration Date'),
        f.StringField('info', display_name='Comments'),
        f.DateTimeField('modified', display_name='Modified'),
        f.StringField('name', display_name='Name'),
        f.LinkField('zone', display_name='Zone', link_to='Zone'),
    ]
    _views = {'all': ['name', 'zone', 'active', 'auto_update', 'created', 'modified', 'expiration', 'info'], 'brief': ['name', 'zone']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name', 'zone']])
        return l.strip()

    @property
    def devices(self):
        cls = getattr(pynetdot.models, 'Device')
        return cls.search(name=self.id)

    @property
    def a_records(self):
        cls = getattr(pynetdot.models, 'RRADDR')
        return cls.search(rr=self.id)

    @property
    def cnames(self):
        cls = getattr(pynetdot.models, 'RRCNAME')
        return cls.search(rr=self.id)

    @property
    def ds_records(self):
        cls = getattr(pynetdot.models, 'RRDS')
        return cls.search(rr=self.id)

    @property
    def hinfo_records(self):
        cls = getattr(pynetdot.models, 'RRHINFO')
        return cls.search(rr=self.id)

    @property
    def loc_records(self):
        cls = getattr(pynetdot.models, 'RRLOC')
        return cls.search(rr=self.id)

    @property
    def mx_records(self):
        cls = getattr(pynetdot.models, 'RRMX')
        return cls.search(rr=self.id)

    @property
    def naptr_records(self):
        cls = getattr(pynetdot.models, 'RRNAPTR')
        return cls.search(rr=self.id)

    @property
    def ns_records(self):
        cls = getattr(pynetdot.models, 'RRNS')
        return cls.search(rr=self.id)

    @property
    def ptr_records(self):
        cls = getattr(pynetdot.models, 'RRPTR')
        return cls.search(rr=self.id)

    @property
    def srv_records(self):
        cls = getattr(pynetdot.models, 'RRSRV')
        return cls.search(rr=self.id)

    @property
    def txt_records(self):
        cls = getattr(pynetdot.models, 'RRTXT')
        return cls.search(rr=self.id)


class BaseRRADDR(n.Netdot):
    '''
    A DNS "A" record makes a connection between a domain name and an IPv4
    address.  A "AAAA" record does the same thing, but with IPv6 addresses. A
    "dual-stack" host can have both an A record and a AAAA record at the same
    time.
    '''
    resource = 'RRADDR/'
    id_field = 'id'
    _fields = [
        f.LinkField('ipblock', display_name='Ipblock', link_to='Ipblock'),
        f.LinkField('rr', display_name='Resource Record', link_to='RR'),
        f.StringField('ttl', display_name='TTL'),
    ]
    _views = {'all': ['ipblock', 'rr', 'ttl'], 'brief': ['rr', 'ipblock']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['ipblock', 'rr']])
        return l.strip()


class BaseRRCNAME(n.Netdot):
    '''
    DNS CNAME records map an alias or nickname to the real or Canonical name
    which may lie outside the current zone. Canonical means expected or real
    name.
    '''
    resource = 'RRCNAME/'
    id_field = 'id'
    _fields = [
        f.StringField('cname', display_name='CNAME'),
        f.LinkField('rr', display_name='Alias', link_to='RR'),
        f.StringField('ttl', display_name='TTL'),
    ]
    _views = {'all': ['rr', 'cname', 'ttl'], 'brief': ['rr', 'cname']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['rr', 'cname']])
        return l.strip()


class BaseRRDS(n.Netdot):
    '''
    The DS Resource Record refers to a DNSKEY RR and is used in the DNS DNSKEY
    authentication process.  A DS RR refers to a DNSKEY RR by storing the key
    tag, algorithm number, and a digest of the DNSKEY RR.
    '''
    resource = 'RRDS/'
    id_field = 'id'
    _fields = [
        f.IntegerField('algorithm', display_name='Algorithm'),
        f.StringField('digest', display_name='Digest'),
        f.IntegerField('digest_type', display_name='Digest Type'),
        f.IntegerField('key_tag', display_name='Key Tag'),
        f.LinkField('rr', display_name='Resource Record', link_to='RR'),
        f.StringField('ttl', display_name='TTL'),
    ]
    _views = {'all': ['rr', 'ttl', 'key_tag', 'algorithm', 'digest_type', 'digest'], 'brief': ['rr', 'ttl', 'key_tag', 'algorithm', 'digest_type', 'digest']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['rr', 'key_tag']])
        return l.strip()


class BaseRRHINFO(n.Netdot):
    '''
    DNS HINFO records are used to acquire general information about a host.
    The main use is for protocols such as FTP that can use special procedures
    when talking between machines or operating systems of the same type.
    These may also be useful just for inventory purposes.  Publishing HINFO
    records may pose a security risk, thus Netdot administrators may choose
    not to include these records when exporting zone data
    '''
    resource = 'RRHINFO/'
    id_field = 'id'
    _fields = [
        f.StringField('cpu', display_name='CPU'),
        f.StringField('os', display_name='OS'),
        f.LinkField('rr', display_name='Resource Record', link_to='RR'),
        f.StringField('ttl', display_name='TTL'),
    ]
    _views = {'all': ['cpu', 'os', 'rr', 'ttl'], 'brief': ['cpu', 'os', 'rr']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['cpu', 'os', 'rr']])
        return l.strip()


class BaseRRLOC(n.Netdot):
    '''
    Location Information. See RFC1876
    '''
    resource = 'RRLOC/'
    id_field = 'id'
    _fields = [
        f.IntegerField('altitude', display_name='Altitude'),
        f.StringField('horiz_pre', display_name='Horizontal Precision'),
        f.IntegerField('latitude', display_name='Latitude'),
        f.IntegerField('longitude', display_name='Longitude'),
        f.LinkField('rr', display_name='Resource Record', link_to='RR'),
        f.StringField('size', display_name='Size'),
        f.StringField('ttl', display_name='TTL'),
        f.StringField('vert_pre', display_name='Vertical Precision'),
    ]
    _views = {'all': ['rr', 'size', 'horiz_pre', 'vert_pre', 'latitude', 'longitude', 'altitude'], 'brief': ['rr', 'latitude', 'longitude', 'altitude']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['rr']])
        return l.strip()


class BaseRRMX(n.Netdot):
    '''
    A mail exchanger record (MX record) is a type of resource record in the
    Domain Name System that specifies a mail server responsible for accepting
    email messages on behalf of a recipient's domain and a preference value
    used to prioritize mail delivery if multiple mail servers are available.
    The set of MX records of a domain name specifies how email should be
    routed with the Simple Mail Transfer Protocol.
    '''
    resource = 'RRMX/'
    id_field = 'id'
    _fields = [
        f.StringField('exchange', display_name='Exchange'),
        f.IntegerField('preference', display_name='Preference'),
        f.LinkField('rr', display_name='Resource Record', link_to='RR'),
        f.StringField('ttl', display_name='TTL'),
    ]
    _views = {'all': ['preference', 'exchange', 'rr', 'ttl'], 'brief': ['preference', 'exchange', 'rr']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['preference', 'exchange', 'rr']])
        return l.strip()


class BaseRRNAPTR(n.Netdot):
    '''
    Naming Authority Pointer (NAPTR) Resource Record (RFC3403)
    '''
    resource = 'RRNAPTR/'
    id_field = 'id'
    _fields = [
        f.StringField('flags', display_name='Flags'),
        f.IntegerField('order_field', display_name='Order'),
        f.IntegerField('preference', display_name='Preference'),
        f.StringField('regexpr', display_name='Regexp'),
        f.StringField('replacement', display_name='Replacement'),
        f.LinkField('rr', display_name='Resource Record', link_to='RR'),
        f.StringField('services', display_name='Services'),
        f.StringField('ttl', display_name='TTL'),
    ]
    _views = {'all': ['order_field', 'preference', 'flags', 'services', 'regexpr', 'replacement', 'rr', 'ttl'], 'brief': ['rr', 'services', 'regexpr', 'replacement']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['rr', 'services', 'regexpr', 'replacement']])
        return l.strip()


class BaseRRNS(n.Netdot):
    '''
    DNS NS Record
    '''
    resource = 'RRNS/'
    id_field = 'id'
    _fields = [
        f.StringField('nsdname', display_name='Name Server'),
        f.LinkField('rr', display_name='Resource Record', link_to='RR'),
        f.StringField('ttl', display_name='TTL'),
    ]
    _views = {'all': ['nsdname', 'rr', 'ttl'], 'brief': ['nsdname', 'rr']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['nsdname', 'rr']])
        return l.strip()


class BaseRRPTR(n.Netdot):
    '''
    A PTR record is the reverse of an A record. That is, it maps an IP address
    to a hostname, rather than vice versa.
    '''
    resource = 'RRPTR/'
    id_field = 'id'
    _fields = [
        f.LinkField('ipblock', display_name='IP', link_to='Ipblock'),
        f.StringField('ptrdname', display_name='Domain Name'),
        f.LinkField('rr', display_name='Resource Record', link_to='RR'),
        f.StringField('ttl', display_name='TTL'),
    ]
    _views = {'all': ['rr', 'ipblock', 'ptrdname', 'ttl'], 'brief': ['rr', 'ipblock', 'ptrdname']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['rr', 'ipblock', 'ptrdname']])
        return l.strip()


class BaseRRSRV(n.Netdot):
    '''
    DNS SRV Record (RFC 2782)
    '''
    resource = 'RRSRV/'
    id_field = 'id'
    _fields = [
        f.IntegerField('port', display_name='Port'),
        f.IntegerField('priority', display_name='Priority'),
        f.LinkField('rr', display_name='Name', link_to='RR'),
        f.StringField('target', display_name='Target'),
        f.StringField('ttl', display_name='TTL'),
        f.IntegerField('weight', display_name='Weight'),
    ]
    _views = {'all': ['rr', 'ttl', 'priority', 'weight', 'port', 'target'], 'brief': ['rr', 'priority', 'weight', 'port', 'target']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['rr', 'target']])
        return l.strip()


class BaseRRTXT(n.Netdot):
    '''
    DNS TXT records are used to hold descriptive text.  The semantics of the
    text depends on the domain where it is found.
    '''
    resource = 'RRTXT/'
    id_field = 'id'
    _fields = [
        f.LinkField('rr', display_name='Resource Record', link_to='RR'),
        f.StringField('ttl', display_name='TTL'),
        f.StringField('txtdata', display_name='Text'),
    ]
    _views = {'all': ['txtdata', 'rr', 'ttl'], 'brief': ['txtdata', 'rr']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['txtdata', 'rr']])
        return l.strip()


class BaseService(n.Netdot):
    '''
    An Internet service
    '''
    resource = 'Service/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
    ]
    _views = {'all': ['name', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def Ips(self):
        cls = getattr(pynetdot.models, 'IpService')
        return cls.search(service=self.id)


class BaseSite(n.Netdot):
    '''
    A physical location such as a building or data center.
    '''
    resource = 'Site/'
    id_field = 'id'
    _fields = [
        f.StringField('aliases', display_name='Aliases'),
        f.LinkField('availability', display_name='Availability', link_to='Availability'),
        f.StringField('city', display_name='City'),
        f.LinkField('contactlist', display_name='Contact List', link_to='ContactList'),
        f.StringField('country', display_name='Country'),
        f.IntegerField('gsf', display_name='GSF'),
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
        f.StringField('number', display_name='Site ID'),
        f.StringField('pobox', display_name='P.O. Box'),
        f.StringField('state', display_name='State'),
        f.StringField('street1', display_name='Street (1)'),
        f.StringField('street2', display_name='Street (2)'),
        f.StringField('zip', display_name='Zip/Postal Code'),
    ]
    _views = {'all': ['name', 'number', 'gsf', 'aliases', 'street1', 'street2', 'pobox', 'city', 'state', 'zip', 'country', 'availability', 'contactlist', 'info'], 'brief': ['name', 'number', 'street1', 'city']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name', 'aliases']])
        return l.strip()

    @property
    def farlinks(self):
        cls = getattr(pynetdot.models, 'SiteLink')
        return cls.search(farend=self.id)

    @property
    def nearlinks(self):
        cls = getattr(pynetdot.models, 'SiteLink')
        return cls.search(nearend=self.id)

    @property
    def devices(self):
        cls = getattr(pynetdot.models, 'Device')
        return cls.search(site=self.id)

    @property
    def entities(self):
        cls = getattr(pynetdot.models, 'EntitySite')
        return cls.search(site=self.id)

    @property
    def floors(self):
        cls = getattr(pynetdot.models, 'Floor')
        return cls.search(site=self.id)

    @property
    def people(self):
        cls = getattr(pynetdot.models, 'Person')
        return cls.search(location=self.id)

    @property
    def subnets(self):
        cls = getattr(pynetdot.models, 'SiteSubnet')
        return cls.search(site=self.id)


class BaseSiteLink(n.Netdot):
    '''
    A Link between two Sites.  A Site Link can consist of one or more circuits
    '''
    resource = 'SiteLink/'
    id_field = 'id'
    _fields = [
        f.LinkField('entity', display_name='Entity', link_to='Entity'),
        f.LinkField('farend', display_name='Destination (Site)', link_to='Site'),
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
        f.LinkField('nearend', display_name='Origin (Site)', link_to='Site'),
    ]
    _views = {'all': ['name', 'entity', 'nearend', 'farend', 'info'], 'brief': ['name', 'entity', 'nearend', 'farend']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def circuits(self):
        cls = getattr(pynetdot.models, 'Circuit')
        return cls.search(linkid=self.id)


class BaseSiteSubnet(n.Netdot):
    '''
    Site to Subnet join table
    '''
    resource = 'SiteSubnet/'
    id_field = 'id'
    _fields = [
        f.LinkField('site', display_name='Site', link_to='Site'),
        f.LinkField('subnet', display_name='Subnet', link_to='Ipblock'),
    ]
    _views = {'all': ['subnet', 'site'], 'brief': ['subnet', 'site']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['subnet', 'site']])
        return l.strip()


class BaseSplice(n.Netdot):
    '''
    Cable Splices
    '''
    resource = 'Splice/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name=''),
        f.LinkField('strand1', display_name='', link_to='CableStrand'),
        f.LinkField('strand2', display_name='', link_to='CableStrand'),
    ]
    _views = {'all': ['strand1', 'strand2'], 'brief': ['strand1', 'strand2']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['strand1', 'strand2']])
        return l.strip()


class BaseSTPInstance(n.Netdot):
    '''
    Spanning Tree Protocol Instance
    '''
    resource = 'STPInstance/'
    id_field = 'id'
    _fields = [
        f.IntegerField('bridge_priority', display_name='Bridge Priority'),
        f.LinkField('device', display_name='Device', link_to='Device'),
        f.IntegerField('number', display_name='Number'),
        f.StringField('root_bridge', display_name='Root Bridge'),
        f.IntegerField('root_port', display_name='Root Port'),
    ]
    _views = {'all': ['number', 'device', 'root_port', 'root_bridge', 'bridge_priority'], 'brief': ['number', 'device', 'root_port', 'root_bridge', 'bridge_priority']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['number', 'device']])
        return l.strip()

    @property
    def stp_ports(self):
        cls = getattr(pynetdot.models, 'InterfaceVlan')
        return cls.search(stp_instance=self.id)


class BaseStrandStatus(n.Netdot):
    '''
    Cable strand/pair status
    '''
    resource = 'StrandStatus/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name=''),
        f.StringField('name', display_name=''),
    ]
    _views = {'all': ['name'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def strands(self):
        cls = getattr(pynetdot.models, 'CableStrand')
        return cls.search(status=self.id)


class BaseSubnetZone(n.Netdot):
    '''
    IP Subnet to DNS Zone join table
    '''
    resource = 'SubnetZone/'
    id_field = 'id'
    _fields = [
        f.LinkField('subnet', display_name='Subnet', link_to='Ipblock'),
        f.LinkField('zone', display_name='Zone', link_to='Zone'),
    ]
    _views = {'all': ['subnet', 'zone'], 'brief': ['subnet', 'zone']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['subnet', 'zone']])
        return l.strip()


class BaseVlan(n.Netdot):
    '''
    A Virtual LAN
    '''
    resource = 'Vlan/'
    id_field = 'id'
    _fields = [
        f.StringField('description', display_name='Description'),
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
        f.IntegerField('vid', display_name='VLAN ID'),
        f.LinkField('vlangroup', display_name='Group', link_to='VlanGroup'),
    ]
    _views = {'all': ['vid', 'name', 'vlangroup', 'description', 'info'], 'brief': ['vid', 'name', 'description']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['vid']])
        return l.strip()

    @property
    def interfaces(self):
        cls = getattr(pynetdot.models, 'InterfaceVlan')
        return cls.search(vlan=self.id)

    @property
    def subnets(self):
        cls = getattr(pynetdot.models, 'Ipblock')
        return cls.search(vlan=self.id)


class BaseVlanGroup(n.Netdot):
    '''
    A Virtual LAN Group
    '''
    resource = 'VlanGroup/'
    id_field = 'id'
    _fields = [
        f.StringField('description', display_name='Description'),
        f.IntegerField('end_vid', display_name='End'),
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Name'),
        f.IntegerField('start_vid', display_name='Start'),
    ]
    _views = {'all': ['name', 'start_vid', 'end_vid', 'description', 'info'], 'brief': ['name', 'description', 'start_vid', 'end_vid']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def vlans(self):
        cls = getattr(pynetdot.models, 'Vlan')
        return cls.search(vlangroup=self.id)


class BaseZone(n.Netdot):
    '''
    A DNS Zone
    '''
    resource = 'Zone/'
    id_field = 'id'
    _fields = [
        f.BoolField('active', display_name='Active?'),
        f.LinkField('contactlist', display_name='Contact List', link_to='ContactList'),
        f.IntegerField('default_ttl', display_name='Default TTL'),
        f.IntegerField('expire', display_name='Expire'),
        f.StringField('export_file', display_name='Export File'),
        f.StringField('include', display_name='Include'),
        f.StringField('info', display_name='Comments'),
        f.IntegerField('minimum', display_name='Minimum'),
        f.StringField('mname', display_name='Server Name'),
        f.StringField('name', display_name='Domain Name'),
        f.IntegerField('refresh', display_name='Refresh'),
        f.IntegerField('retry', display_name='Retry'),
        f.StringField('rname', display_name='Mail Box'),
        f.IntegerField('serial', display_name='Serial'),
    ]
    _views = {'all': ['name', 'mname', 'rname', 'serial', 'refresh', 'retry', 'expire', 'minimum', 'contactlist', 'active', 'export_file', 'default_ttl', 'include', 'info'], 'brief': ['name']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()

    @property
    def records(self):
        cls = getattr(pynetdot.models, 'RR')
        return cls.search(zone=self.id)

    @property
    def subnets(self):
        cls = getattr(pynetdot.models, 'SubnetZone')
        return cls.search(zone=self.id)

    @property
    def aliases(self):
        cls = getattr(pynetdot.models, 'ZoneAlias')
        return cls.search(zone=self.id)


class BaseZoneAlias(n.Netdot):
    '''
    An alias of an existing zone
    '''
    resource = 'ZoneAlias/'
    id_field = 'id'
    _fields = [
        f.StringField('info', display_name='Comments'),
        f.StringField('name', display_name='Domain Name'),
        f.LinkField('zone', display_name='Zone', link_to='Zone'),
    ]
    _views = {'all': ['name', 'zone', 'info'], 'brief': ['name', 'zone']}

    @property
    def label(self):
        l = ' '.join([unicode(getattr(self, l)) for l in ['name']])
        return l.strip()



