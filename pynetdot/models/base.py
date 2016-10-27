import pynetdot.netdot as n
import pynetdot.fields as f
import pynetdot.models

class BaseArpCache(n.Netdot):
    """
    Device ARP Cache

    Attributes:
        device: Device where this Arp Cache was found
        tstamp: When this Cache was collected
        entries: List of ArpCacheEntry objects
    """
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
    """
    ARP Cache Entry

    Attributes:
        arpcache: ARP Cache where this entry belongs
        interface: Interface
        ipaddr: IP address
        physaddr: Physical Address (MAC)
    """
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
    """
    Autonomous System Number

    Attributes:
        description: A short description of this ASN
        info: Comments
        number: Autonomous System (AS) Number
        rir: Regional Internet Registry from which ASN was obtained (AFRINIC, APNIC, ARIN, LACNIC, RIPE)
        devices: List of Device objects
        ipblocks: List of Ipblock objects
    """
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
    """
    Assets represent network hardware (devices or modules). If an asset is
    installed, it will be associated with a device or devicemodule object.

    Attributes:
        custom_serial: Custom (human-set) serial number of this asset
        date_purchased: The date the asset was purchased
        description: A short description for this Asset
        info: Comments
        inventory_number: Asset inventory number
        maint_contract: Reference to a maintenance or support contract with hardware vendor or third party.
        maint_from: Device covered in maintenance from this date (YYYY-MM-DD)
        maint_until: Device covered in maintenance until this date (YYYY-MM-DD)
        physaddr: The base MAC address of this Asset.
        po_number: Purchase order number
        product_id: product key
        reserved_for: For hardware that is not installed, specify if it is reserved and what for
        serial_number: Asset serial number
        devices: List of Device objects
        device_modules: List of DeviceModule objects
    """
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
    """
    Audit Table to record database operations made by users

    Attributes:
        fields: Fields changed
        label: Object Label
        object_id: Object id
        operation: DB Operation (insert, update, delete)
        tablename: Table affected
        tstamp: When this change happened
        username: User that made the change
        vals: Values that changed
    """
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
    """
    A Time Period

    Attributes:
        info: Comments
        name: Time period brief description. e.g. "24x7"
        page_notifications: List of Contact objects
        page_notifications: List of Contact objects
        page_notifications: List of Contact objects
        entities: List of Entity objects
        sites: List of Site objects
    """
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
    """
    A Backbone cable that interconnects two sites.  Backbone cables can have
    multiple strands.

    Attributes:
        end_closet: Closet where this cable terminates
        info: Comments
        installdate: Date when this Cable was first installed (YYYY-MM-DD)
        length: The physical length of this cable
        name: A name given to this cable.
        owner: Entity that owns this cable
        start_closet: Closet where this cable originates
        type: The type of cable
        strands: List of CableStrand objects
    """
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
    """
    A BGP Peering

    Attributes:
        authkey: The authentication key for this BGP session
        bgppeeraddr: BGP Peer Address
        bgppeerid: BGP Peer ID
        contactlist: Who to contact about this peering session. Also used for Nagios alarms.
        device: Device where BGP peering exists (the local device, that is)
        entity: Entity with which Peering Exists
        info: Comments
        last_changed: Time when the state last changed
        max_v4_prefixes: Maximum number of IPv4 prefixes we will permit from this peer
        max_v6_prefixes: Maximum number of IPv6 prefixes we will permit from this peer
        monitored: Flag that specifies if this peering should be monitored
        peer_group: Name of the peer group
        state: Peering state
    """
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
    """
    A single cable strand/pair

    Attributes:
        cable: Cable to which this strand belongs
        circuit_id: ID of the circuit which this strand is a part of
        description: A text description of this strand
        fiber_type: The type of fiber that this strand is made of
        info: Comments
        name: A name for this strand
        number: The numeric order of this strand
        status: Status of this strand
        splices: List of Splice objects
        splices2: List of Splice objects
    """
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
    """
    Types of Cables

    Attributes:
        info: Comments
        name: The name of this cable type
        backbonecables: List of BackboneCable objects
        horizontalcables: List of HorizontalCable objects
    """
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
    """
    A circuit can either be a WAN link provided by an external entity, or a
    set of [spliced] backbone cable strands terminated into two device
    interfaces

    Attributes:
        cid: ID of this circuit.
        datetested: Date that this circuit was last tested (YYYY-MM-DD)
        info: Comments
        installdate: Date when this circuit was installed (YYYY-MM-DD)
        linkid: Site Link to which this circuit belongs
        loss: Tested loss (dbm)
        speed: The speed of this circuit (Mbps)
        status: Status of this circuit
        type: The type of this circuit
        vendor: Who provides this circuit, if it is not internal
        strands: List of CableStrand objects
        interfaces: List of Interface objects
    """
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
    """
    Circuit status

    Attributes:
        info: Comments
        name: Circuit Status
        circuits: List of Circuit objects
    """
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
    """
    Circuit Type

    Attributes:
        info: Comments
        name: Circuit Type
        circuits: List of Circuit objects
    """
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
    """
    A Communications Closet.  A Closet is different from a normal Room in two
    ways: a) Backbone Cables (inter and intra building) terminate in Closets.
    b) Horizontal Cables _start_ in Closets and _end_ in Rooms

    Attributes:
        access_key_type: 
        asbestos_tiles: 
        catv_taps: 
        converted_patch_panels: 
        dimensions: 
        ground_buss: 
        hvac_type: 
        info: 
        name: An identifier for this Closet within a Site
        ot_blocks: 
        outlets: 
        pair_count: 
        patch_panels: 
        rack_type: 
        racks: 
        room: The Room number where the closet is located
        ru_avail: 
        shared_with: 
        ss_blocks: 
        work_needed: 
        backbones_end: List of BackboneCable objects
        backbones_start: List of BackboneCable objects
        horizontalcables: List of HorizontalCable objects
    """
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
    """
    A Contact object is basically a Role of a certain Person.  People can be
    associated with one or more resources (devices, services, etc) for which
    they could be contacted.  Each Contact object represents one of these
    roles.

    Attributes:
        contactlist: The list or group of Contacts to which this Contact belongs
        contacttype: The type of this Contact
        escalation_level: This level defines when this contact will be notified when monitoring devices or services.  Notifications usually escalate to a different set of contacts when the problem is not resolved in a certain amount of time.  This logic is implemented by the chosen external monitoring tool, not Netdot.
        info: Comments
        notify_email: Set this field to the desired Time Period to receive e-mail notifications when monitoring devices or services
        notify_pager: Set this field to the desired Time Period to receive pager notifications when monitoring devices or services
        notify_voice: Set this field to the desired Time Period to receive voice notifications when monitoring devices or services
        person: The actual Person that this contact refers to.  The Person table holds the actual contact information
    """
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
    """
    A list of contacts

    Attributes:
        info: Comments
        name: Name for this group
        peerings: List of BGPPeering objects
        contacts: List of Contact objects
        devices: List of DeviceContacts objects
        entities: List of Entity objects
        access_rights: List of GroupRight objects
        outlets: List of HorizontalCable objects
        interfaces: List of Interface objects
        services: List of IpService objects
        sites: List of Site objects
        zones: List of Zone objects
    """
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
    """
    Type of contact

    Attributes:
        info: Comments
        name: The name for this Contact Type
        contacts: List of Contact objects
    """
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
    """
    A network device.  Particularly, Devices in Netdot are network
    infrastructure devices that network administrators care about for
    inventory, monitoring and management purposes.  Not to be confused with
    end nodes

    Attributes:
        aliases: Other names by which this Device is known
        asset_id: asset fk
        auto_dns: Whether a DNS name should be auto generated for each IP address in this device
        bgpid: Border Gateway Protocol ID.  This usually has the form of an IP address
        bgplocalas: Border Gateway Protocol Local Autonomous System number
        canautoupdate: If SNMP updates are automated, this value determines whether this Device should be included
        collect_arp: Whether Netdot should collect ARP cache data from this Device.  Notice that this is mostly intended for Routers, though not necessarily
        collect_fwt: Whether Netdot should collect bridge Forwarding Table (FWT) data from this Device
        collect_stp: Enable or Disable querying device for Spanning Tree information
        community: SNMP community
        customer_managed: Does the operation of this Device fall into the responsibility of the customer (or "user" Entity)?
        date_installed: Date that this Device was installed, or first seen in the network
        down_from: Device in down time from this date (YYYY-MM-DD)
        down_until: Device in down time until this date (YYYY-MM-DD)
        extension: IP phone extension
        host_device: Another device which this one is part of, such as a virtual machine host. Host device will be used as parent device in monitoring exports.
        info: Comments
        ipforwarding: Whether this device has IP forwarding enabled (IP-MIB::ipForwarding.0)
        last_arp: Last time ARP cache data was collected from this Device
        last_fwt: Last time Forwarding Tables (FWT) were collected from this Device
        last_updated: Date that this Device was last updated
        layers: Each digit represents a layer of the OSI model served by the device
        monitor_config: Indicates whether this Device should be included in configuration management tools (i.e. RANCID)
        monitor_config_group: Configuration Management group (i.e. RANCID group)
        monitored: Determines if this Device should be included in the configurations for monitoring software
        monitoring_path_cost: Netdot uses a variant of the Dijkstra algorithm to determine monitoring dependencies. Results can be affected adversely, for instance, by passive devices with connections that are not actually passing traffic.  This value allows the administrator to set a higher cost for those devices, for the purpose of influencing the determination of monitoring paths.
        monitoring_template: A template that defines common monitoring parameters for a group of devices. (E.g. a Nagios template to inherit from)
        monitorstatus: The monitoring status of this Device.  This values is supposed to be fed back into Netdot by an external process
        name: The Device name is a reference to a DNS Resource Record (RR)
        oobname: A name or command used to connect to this Device via an Out of Band connection, such as a Console Server
        oobname_2: A name or command used to connect to this Device via an Out of Band connection, such as a Console Server
        oobnumber: A phone number used to connect to this Device via an Out of Band modem
        oobnumber_2: A phone number used to connect to this Device via an Out of Band modem
        os: Operating System name and version
        owner: Entity that owns this Device
        power_outlet: ID of the power outlet in a power distribution unit or similar
        power_outlet_2: ID of the power outlet in a power distribution unit or similar
        rack: Rack ID where this Device is physically installed
        room: Room where this Device is installed
        site: Site or Building where this Device is located.  This is set manually.
        snmp_authkey: SNMPv3 Authentication Key
        snmp_authprotocol: SNMPv3 Authentication Protocol (MD5|SHA)
        snmp_bulk: Enable or Disable SNMP BULK operations for this device
        snmp_conn_attempts: How many times Netdot has attempted, and failed, to contact this device via SNMP
        snmp_down: Whether Netdot has tried more than MAX_SNMP_CONNECTION_ATTEMPTS times to update this device via SNMP
        snmp_managed: Enable or Disable SNMP operations on this device
        snmp_polling: Enable or Disable SNMP polling from management tools which get their configurations from Netdot
        snmp_privkey: SNMPv3 Privacy Key
        snmp_privprotocol: SNMPv3 Privacy Protocol (AES|DES)
        snmp_securitylevel: SNMPv3 Security Level (noAuthNoPriv|authNoPriv|authPriv)
        snmp_securityname: SNMPv3 user name
        snmp_target: SNMP target IP address.  Netdot will try to always use this IP address when snmp-querying the device
        snmp_version: Simple Network Management Protocol Version (1|2|3)
        stp_enabled: Whether some version of the Spanning Tree Protocol is enabled on this switch
        stp_mst_digest: Multiple Spanning Tree (MST) Configuration Digest
        stp_mst_region: Multiple Spanning Tree (MST) region name
        stp_mst_rev: Multiple Spanning Tree (MST) revision
        stp_type: Spanning Tree Protocol Type (802.1d, MST, PVST, etc)
        sysdescription: System Description.  Meanto be populated by SNMP
        syslocation: System Location.  Meant to be populated by SNMP.
        sysname: System Name.  Meant to be populated by SNMP.
        used_by: Entity that uses this Device
        arp_caches: List of ArpCache objects
        bgppeers: List of BGPPeering objects
        hosted_devices: List of Device objects
        attributes: List of DeviceAttr objects
        modules: List of DeviceModule objects
        contacts: List of DeviceContacts objects
        forwarding_tables: List of FWTable objects
        interfaces: List of Interface objects
        stp_instances: List of STPInstance objects
    """
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
    """
    A Device Attribute

    Attributes:
        device: Device to which this attribute is assigned
        name: Name of this attribute
        value: Value for this attribute
    """
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
    """
    A Device Attributes Name

    Attributes:
        info: 
        name: 
        attributes: List of DeviceAttr objects
    """
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
    """
    Device to Contactlist join table

    Attributes:
        contactlist: 
        device: 
    """
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
    """
    A Device Physical Entity

    Attributes:
        asset_id: asset fk
        class: Module Class
        contained_in: The number for the physical entity which "contains" this physical entity
        date_installed: Date when this module was installed/discovered
        description: A textual description of physical entity
        device: Device where this Module belongs
        fru: Whether or not this physical entity is considered a "Field Replaceable Unit" by the vendor.
        fw_rev: The vendor-specific firmware revision string for the physical entity
        hw_rev: The vendor-specific hardware revision string for the physical entity
        last_updated: Date when this module was installed/discovered
        model: The vendor-specific model name identifier string associated with this physical component
        name: The textual name of the physical entity
        number: Module index number
        pos: An indication of the relative position of this child component among all its sibling components
        sw_rev: The vendor-specific software revision string for the physical entity
        type: An indication of the vendor-specific hardware type of the physical entity
    """
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
    """
    A DHCP Attribute or Parameter

    Attributes:
        name: Name of this attribute
        scope: DHCP scope where this attribute will be applied
        value: Value for this attribute
    """
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
    """
    A DHCP Attributes Name

    Attributes:
        code: 
        format: 
        info: 
        name: 
        attributes: List of DhcpAttr objects
    """
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
    """
    A DHCP Scope

    Attributes:
        active: Should this scope be included in the DHCP files generated by Netdot?
        container: Reference to the container (parent) scope in the hierarchy.  Global scopes are at the top.
        duid: DHCP Unique Identifier. Only applies to host scopes. See RFC 3315
        enable_failover: Enable Failover for this Subnet scope or by default for all Subnet scopes within this Global scope.
        export_file: Path and file name to export config to.
        failover_peer: Name of failover peer to assign to pools by default.  Valid in Subnet and Global scopes.  Subnet scope value takes precedence.
        ipblock: Reference to an IPblock object.  This only applies to host and subnet scopes.
        name: Name of the Scope.  For example, a host name is the name of a scope of type "host".
        physaddr: Reference to a MAC object.  Only useful within host scopes.
        text: The contents of this field will be included in the configuration file.
        type: Type of this scope.
        version: IP version (4 or 6). Only applies to global scopes
        attributes: List of DhcpAttr objects
        contained_scopes: List of DhcpScope objects
        templates: List of DhcpScopeUse objects
        derived_scopes: List of DhcpScopeUse objects
    """
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
    """
    A DHCP Scope Type

    Attributes:
        info: 
        name: The name of this Scope type.
        scopes: List of DhcpScope objects
    """
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
    """
    Relationship between a scopes and scope templates

    Attributes:
        scope: DHCP scope where template will be used
        template: DHCP template scope
    """
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
    """
    An organization related to the network in some way

    Attributes:
        acctnumber: 
        aliases: Other names by which this Entity is known
        asname: The Autonomous System Name of this Peer Entity
        asnumber: The Autonomous System Number of this Peer Entity
        availability: Time Period at which this Entity is available
        config_type: Device type to use when monitoring configuration with tools such as RANCID
        contactlist: 
        info: Comments
        maint_contract: 
        name: Name of this Entity
        oid: The Enterprise Object ID is a unique value assigned to an Entity to use in their SNMP agents
        short_name: A short name for this Entity
        bgppeers: List of BGPPeering objects
        cables: List of BackboneCable objects
        circuits: List of Circuit objects
        links: List of SiteLink objects
        owned_devices: List of Device objects
        used_devices: List of Device objects
        roles: List of EntityRole objects
        sites: List of EntitySite objects
        owned_blocks: List of Ipblock objects
        used_blocks: List of Ipblock objects
        maintenance_contracts: List of MaintContract objects
        employees: List of Person objects
        products: List of Product objects
    """
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
    """
    An Entity might play different roles.  For example, the same Entity can be
    both a Customer and a Peer.

    Attributes:
        entity: The Entity that performs this role.
        type: A type of Entity.
    """
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
    """
    Entity to Site join table

    Attributes:
        entity: 
        site: 
    """
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
    """
    Types of Entities

    Attributes:
        info: 
        name: 
        roles: List of EntityRole objects
    """
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
    """
    Types of Fiber

    Attributes:
        info: 
        name: A name for this Fiber Type
        strands: List of CableStrand objects
    """
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
    """
    Floor Table

    Attributes:
        info: 
        level: 
        site: 
        rooms: List of Room objects
    """
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
    """
    Bridge Forwarding Table.  One of these is created every time a Device is
    queried.  Entries in these tables contain physical addresses and the ports
    where they have been seen.

    Attributes:
        device: 
        tstamp: 
        entries: List of FWTableEntry objects
    """
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
    """
    Bridge Forwarding Table entry

    Attributes:
        fwtable: 
        interface: 
        physaddr: 
    """
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
    """
    Join between a ContactList and its Access Rights

    Attributes:
        accessright: 
        contactlist: 
    """
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
    """
    Horizontal Cable

    Attributes:
        account: An internal account number to which the installation of this cable should be billed to
        closet: The communications closet where this cable originates
        contactlist: A group of people that manages this cable
        datetested: Date this cable was last tested (YYYY-MM-DD)
        faceplateid: ID of the faceplate where this cable is terminated
        info: Comments
        installdate: Date this cable was installed (YYYY-MM-DD)
        jackid: ID of the Jack where this cable is terminated
        length: Length of this cable
        room: Room where this cable terminates
        testpassed: Cable test result (pass/fail)
        type: Type of this cable
        interfaces: List of Interface objects
    """
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
    """
    DNS and DHCP changes

    Attributes:
        pending: This flag specifies whether the change is pending or it has been committed.
        scope: Name of DHCP scope where change happened
        tstamp: When this change happened
        zone: Name of zone where change happened
    """
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
    """
    An interface associated with a device

    Attributes:
        admin_duplex: Administrative status of the Duplex setting on this Interface
        admin_status: Administrative status of this Interface
        auto_dns: Whether a DNS name should be auto generated for each IP address in this interface
        bpdu_filter_enabled: Whether BPDU filter is enabled on this port
        bpdu_guard_enabled: Whether BPDU Guard is enabled on this port
        circuit: 
        contactlist: 
        description: A short description for this Interface.
        device: Device to which this Interface belongs to
        dlci: Data Link Connection Identifier
        doc_status: The documentation status of this interface.  Values: snmp => Discovered by SNMP, manual => Added manually, removed => Was SNMP but it is no longer seen.
        down_from: Interface in down time from this date (YYYY-MM-DD)
        down_until: Interface in down time until this date (YYYY-MM-DD)
        dp_remote_id: Discovery Protocol Remote Device ID.
        dp_remote_ip: Discovery Protocol Remote Device IP address.
        dp_remote_port: Discovery Protocol Remote Device Port.
        dp_remote_type: Discovery Protocol Remote Device Type.
        ignore_ip: Ignore IP address information. Netdot will not insert IP addresses or subnets based on information fro this interface.
        info: Comments
        jack: Reference to a Jack or Cable where this Interface is connected
        jack_char: The ID of the Jack where this Interface is connected
        loop_guard_enabled: Whether Loop guard is enabled on this port
        monitored: Determine whether this Interface should be included in the configuration of an external monitoring software
        monitorstatus: The status of this Interface given by an external monitoring process
        name: The name of this Interface
        neighbor: Another Interface to which this one is physically connected
        neighbor_fixed: Determines whether this link can be modified by automatic topology discovery mechanisms.
        neighbor_missed: Number of times neighbor has not been seen by topology discovery process.  Once MAX_NEIGHBOR_MISSED_TIMES has been reached, the neighbor relationship is removed.
        number: The number of this Interface (usually corresponds to SNMP ifIndex).  In some cases, this value can be a alphanumeric string.
        oper_duplex: Operational Duplex setting
        oper_status: Operational Status of this Interface
        overwrite_descr: Determines whether the description for this Interface should be overwritten via SNMP updates
        physaddr: MAC address of this Interface
        room_char: Room number where this Interface is connected
        root_guard_enabled: Whether Root guard is enabled on this port
        snmp_managed: Determines whether this Interface should be included in the collection of SNMP statistics
        speed: Bits Per Second (bps) speed of which this Interface is capable of
        stp_id: The ID of this port in the Spanning Tree Protocol (dot1dStpPort)
        type: Type of Interface
        arp_entries: List of ArpCacheEntry objects
        fwt_entries: List of FWTableEntry objects
        neighbors: List of Interface objects
        vlans: List of InterfaceVlan objects
        ips: List of Ipblock objects
    """
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
    """
    Interface to VLAN join table

    Attributes:
        interface: 
        stp_des_bridge: The Bridge ID of the bridge that this port considers to be the Designated Bridge for this segment (dot1dStpPortDesignatedBridge)
        stp_des_port: The Port ID of the port on the Designated Bridge for this segment (dot1dStpPortDesignatedPort)
        stp_instance: The Spanning Tree Protocol instance that this port belongs to, for this VLAN
        stp_state: The current Spanning Tree State of this port (dot1dStpPortState). It can be one of: 1 - disabled, 2 - blocking, 3 - listening, 4 - learning, 5 - forwarding, 6 - broken
        vlan: 
    """
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
    """
    An IP (v4 or v6) CIDR block, which can represent both individual addresses
    and blocks of addresses (subnets, etc).

    Attributes:
        address: IP Address.  This value is stored as an integer in the database
        asn: Autonomous System Number where this block originates from
        description: A short description for this IP address or block
        first_seen: Date that this address or block was first seen
        info: Comments
        interface: Device interface where this address is configured
        last_seen: Last time when this address or block was seen
        monitored: Whether this IP address should be monitored or not
        owner: Entity that owns this block
        parent: Smallest IP block that contains this address or block.
        prefix: Prefix length of this IP block
        rir: Regional Internet Registry from which block was obtained (AFRINIC, APNIC, ARIN, LACNIC, RIPE)
        status: Status of this IP block
        use_network_broadcast: Whether the network and broadcast addresses in this IPv4 block should be marked as reserved or not
        used_by: Entity that uses this block
        version: IP version (4 or 6)
        vlan: VLAN to which this subnet is associated
        arp_entries: List of ArpCacheEntry objects
        snmp_devices: List of Device objects
        dhcp_scopes: List of DhcpScope objects
        services: List of IpService objects
        children: List of Ipblock objects
        attributes: List of IpblockAttr objects
        a_records: List of RRADDR objects
        ptr_records: List of RRPTR objects
        sites: List of SiteSubnet objects
        zones: List of SubnetZone objects
    """
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
    """
    An Ipblock Attribute

    Attributes:
        ipblock: Ipblock to which this attribute is assigned
        name: Name of this attribute
        value: Value for this attribute
    """
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
    """
    An Ipblock Attributes Name

    Attributes:
        info: 
        name: 
        attributes: List of IpblockAttr objects
    """
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
    """
    IP block status

    Attributes:
        name: 
        ipblocks: List of Ipblock objects
    """
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
    """
    A relationship between an IP address and a running Internet service

    Attributes:
        contactlist: 
        ip: 
        monitored: 
        monitorstatus: 
        service: 
    """
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
    """
    Device Maintenance Contract

    Attributes:
        info: 
        number: 
        provider: Maintenace Contract Provider
        assets: List of Asset objects
    """
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
    """
    Status information for what is monitored

    Attributes:
        info: 
        name: 
        devices: List of Device objects
        interfaces: List of Interface objects
        ipservices: List of IpService objects
    """
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
    """
    Organizationally Unique Identifier

    Attributes:
        oui: Organizationally Unique Identifier.  Assigned by the IEEE to Ethernet hardware manufacturers.
        vendor: Manufacturer of Ethernet hardware
    """
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
    """
    Information about an individual

    Attributes:
        aliases: Other names by which this Person is known
        cell: Cellular Phone number
        email: E-mail address
        emailpager: Email address used for paging (via a pager gateway)
        entity: The entity that this person works for
        extension: Work Telephone number extension
        fax: Fax number
        firstname: First Name
        home: Home Telephone Number
        info: 
        lastname: Last Name
        location: Site where this Person is located.  The Site is used instead of an Address
        office: Office or Work telephone number
        pager: Pager number
        password: User Password.  Not necessary if this person is not a Netdot user.
        position: Position within the organization
        room: Room where person is located, if available
        user_type: User type
        username: User name.  Only necessary if this person needs access to Netdot.
        roles: List of Contact objects
    """
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
    """
    A physical or MAC address

    Attributes:
        address: A 48 bit MAC address in Hexadecimal digits (with no delimiters)
        first_seen: Time when this address was first seen in the network
        last_seen: Time when this address was last seen in the network
        static: If this value is set, the address is considered permanent and should not be removed, even if it has not been seen in the network for a given amount of time
        arp_entries: List of ArpCacheEntry objects
        assets: List of Asset objects
        dhcp_hosts: List of DhcpScope objects
        fwt_entries: List of FWTableEntry objects
        interfaces: List of Interface objects
        attributes: List of PhysAddrAttr objects
    """
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
    """
    Custom attributes can be assigned to physical (MAC) addresses

    Attributes:
        name: Name of this attribute
        physaddr: Physiscal Address to which this attribute is assigned
        value: Value for this attribute
    """
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
    """
    Custom attribute name for physical (MAC) addresses

    Attributes:
        info: 
        name: 
        attributes: List of PhysAddrAttr objects
    """
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
    """
    Product Names

    Attributes:
        config_type: Device type to use when monitoring configuration with tools such as RANCID
        description: A short description for this Product
        info: Comments
        latest_os: Recommended OS version
        manufacturer: Reference to an Entity which manufactures this product
        name: Product Name
        part_number: Manufacturers part number
        sysobjectid: SNMP Object ID given to this product by its manufacturer
        type: Product Type. Types of network products include routers, switches, hubs, etc.
        assets: List of Asset objects
    """
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
    """
    Types of network devices

    Attributes:
        info: 
        name: 
        products: List of Product objects
    """
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
    """
    Room

    Attributes:
        floor: 
        name: 
        closets: List of Closet objects
        devices: List of Device objects
        jacks: List of HorizontalCable objects
        people: List of Person objects
    """
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
    """
    DNS Resource Record. Also known as the "owner", this object in Netdot
    groups all the records with the same name.

    Attributes:
        active: Should this record be included in the Zone files generated by Netdot?
        auto_update: Determines whether this record can be updated by an automated process.  For example, if a Device Interface changes its name and the change is picked up by an SNMP update
        created: Time when this resource record was created
        expiration: Expiration Date for this Record (YYYY-MM-DD)
        info: Comments
        modified: Last time when this resource record was modified
        name: The identifier for this Record
        zone: Zone or Domain to which this record belongs
        devices: List of Device objects
        a_records: List of RRADDR objects
        cnames: List of RRCNAME objects
        ds_records: List of RRDS objects
        hinfo_records: List of RRHINFO objects
        loc_records: List of RRLOC objects
        mx_records: List of RRMX objects
        naptr_records: List of RRNAPTR objects
        ns_records: List of RRNS objects
        ptr_records: List of RRPTR objects
        srv_records: List of RRSRV objects
        txt_records: List of RRTXT objects
    """
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
    """
    A DNS "A" record makes a connection between a domain name and an IPv4
    address.  A "AAAA" record does the same thing, but with IPv6 addresses. A
    "dual-stack" host can have both an A record and a AAAA record at the same
    time.

    Attributes:
        ipblock: 
        rr: 
        ttl: Record TTL
    """
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
    """
    DNS CNAME records map an alias or nickname to the real or Canonical name
    which may lie outside the current zone. Canonical means expected or real
    name.

    Attributes:
        cname: A domain-name which specifies the canonical or primary name for the owner.
        rr: Alias Name
        ttl: Record TTL
    """
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
    """
    The DS Resource Record refers to a DNSKEY RR and is used in the DNS DNSKEY
    authentication process.  A DS RR refers to a DNSKEY RR by storing the key
    tag, algorithm number, and a digest of the DNSKEY RR.

    Attributes:
        algorithm: The Algorithm field lists the algorithm number of the DNSKEY RR referred to by the DS record. The algorithm number used by the DS RR is identical to the algorithm number used by RRSIG and DNSKEY RRs.
        digest: Digest
        digest_type: The DS RR refers to a DNSKEY RR by including a digest of that DNSKEY RR.  The Digest Type field identifies the algorithm used to construct the digest.
        key_tag: The Key Tag field lists the key tag of the DNSKEY RR referred to by the DS record, in network byte order.
        rr: 
        ttl: Record TTL
    """
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
    """
    DNS HINFO records are used to acquire general information about a host.
    The main use is for protocols such as FTP that can use special procedures
    when talking between machines or operating systems of the same type.
    These may also be useful just for inventory purposes.  Publishing HINFO
    records may pose a security risk, thus Netdot administrators may choose
    not to include these records when exporting zone data

    Attributes:
        cpu: Central Processing Unit
        os: Operating System
        rr: 
        ttl: Record TTL
    """
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
    """
    Location Information. See RFC1876

    Attributes:
        altitude: The altitude of the center of the sphere described by SIZE, in centimeters, from a base of 100,000m below the WGS 84 reference spheroid used by GPS.
        horiz_pre: The horizontal precision of the data, in centimeters, expressed using the same representation as SIZE
        latitude: The latitude of the center of the sphere described by SIZE, in thousandths of a second of arc. 2**31 represents the equator; numbers above that are north latitude.
        longitude: The longitude of the center of the sphere described by SIZE, in thousandths of a second of arc. 2**31 represents the prime meridian; numbers above that are east longitude.
        rr: 
        size: The diameter of a sphere enclosing the described entity.
        ttl: Record TTL
        vert_pre: The vertical precision of the data, in centimeters, expressed using the same representation as SIZE
    """
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
    """
    A mail exchanger record (MX record) is a type of resource record in the
    Domain Name System that specifies a mail server responsible for accepting
    email messages on behalf of a recipient's domain and a preference value
    used to prioritize mail delivery if multiple mail servers are available.
    The set of MX records of a domain name specifies how email should be
    routed with the Simple Mail Transfer Protocol.

    Attributes:
        exchange: A domain-name which specifies a host willing to act as a mail exchange for the owner name. The host name must map directly to one or more address records (A, or AAAA) in the DNS, and must not point to any CNAME records.
        preference: A 16 bit integer which specifies the preference given to this RR among others at the same owner.  Lower values are preferred.
        rr: 
        ttl: Record TTL
    """
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
    """
    Naming Authority Pointer (NAPTR) Resource Record (RFC3403)

    Attributes:
        flags: A <character-string> containing flags to control aspects of the rewriting and interpretation of the fields in the record.  Flags are single characters from the set A-Z and 0-9.  The case of the alphabetic characters is not significant.  The field can be empty.
        order_field: A 16-bit unsigned integer specifying the order in which the NAPTR records MUST be processed in order to accurately represent the ordered list of Rules.  The ordering is from lowest to highest.
        preference: A 16-bit unsigned integer that specifies the order in which NAPTR records with equal Order values SHOULD be processed, low numbers being processed before high numbers
        regexpr: A <character-string> containing a substitution expression that is applied to the original string held by the client in order to construct the next domain name to lookup.  See the DDDS Algorithm specification for the syntax of this field
        replacement: A <domain-name> which is the next domain-name to query for depending on the potential values found in the flags field.  This field is used when the regular expression is a simple replacement operation.  Any value in this field MUST be a fully qualified domain-name
        rr: 
        services: A <character-string> that specifies the Service Parameters applicable to this this delegation path.  It is up to the Application Specification to specify the values found in this field.
        ttl: Record TTL
    """
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
    """
    DNS NS Record

    Attributes:
        nsdname: A domain-name which specifies a host which should be authoritative for the specified class and domain.
        rr: 
        ttl: Record TTL
    """
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
    """
    A PTR record is the reverse of an A record. That is, it maps an IP address
    to a hostname, rather than vice versa.

    Attributes:
        ipblock: 
        ptrdname: A domain-name which points to some location in the domain name space.
        rr: 
        ttl: Record TTL
    """
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
    """
    DNS SRV Record (RFC 2782)

    Attributes:
        port: The port on this target host of this service.  The range is 0-65535
        priority: The priority of this target host.  A client MUST attempt to contact the target host with the lowest-numbered priority it can reach; target hosts with the same priority SHOULD be tried in an order defined by the weight field.  The range is 0-65535
        rr: The domain this SRV record refers to.
        target: The domain name of the target host.  There MUST be one or more address records for this name, the name MUST NOT be an alias (in the sense of RFC 1034 or RFC 2181)
        ttl: Record TTL
        weight: A server selection mechanism.  The weight field specifies a relative weight for entries with the same priority. Larger weights SHOULD be given a proportionately higher probability of being selected. The range of this number is 0-65535
    """
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
    """
    DNS TXT records are used to hold descriptive text.  The semantics of the
    text depends on the domain where it is found.

    Attributes:
        rr: 
        ttl: Record TTL
        txtdata: One or more character-strings
    """
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
    """
    An Internet service

    Attributes:
        info: 
        name: 
        Ips: List of IpService objects
    """
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
    """
    A physical location such as a building or data center.

    Attributes:
        aliases: Alternative names for this site
        availability: Time Period during which people at this Site will be available
        city: City where this Site is located
        contactlist: List of contacts for this Site
        country: Country where this Site is located
        gsf: Gross Square Footage of this site
        info: User Comments
        name: Name given to this site
        number: A unique identifier for this Site within the organization
        pobox: Post Office Box
        state: State where this Site is located
        street1: Street 1st line
        street2: Street 2nd line
        zip: ZIP/Postal Code
        farlinks: List of SiteLink objects
        nearlinks: List of SiteLink objects
        devices: List of Device objects
        entities: List of EntitySite objects
        floors: List of Floor objects
        people: List of Person objects
        subnets: List of SiteSubnet objects
    """
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
    """
    A Link between two Sites.  A Site Link can consist of one or more circuits

    Attributes:
        entity: External Entity which we connect to
        farend: The remote Site for this Link
        info: Comments
        name: A name for this Link
        nearend: The local Site for this Link
        circuits: List of Circuit objects
    """
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
    """
    Site to Subnet join table

    Attributes:
        site: 
        subnet: 
    """
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
    """
    Cable Splices

    Attributes:
        info: 
        strand1: 
        strand2: 
    """
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
    """
    Spanning Tree Protocol Instance

    Attributes:
        bridge_priority: Bridge priority
        device: Device where this STP instance exists
        number: STP Instance number
        root_bridge: Root bridge MAC Address
        root_port: Root port (ifIndex) for this STP instance
        stp_ports: List of InterfaceVlan objects
    """
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
    """
    Cable strand/pair status

    Attributes:
        info: 
        name: 
        strands: List of CableStrand objects
    """
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
    """
    IP Subnet to DNS Zone join table

    Attributes:
        subnet: 
        zone: 
    """
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


class BaseUserType(n.Netdot):
    """
    Types of Netdot users

    Attributes:
        info: 
        name: 
        people: List of Person objects
    """
    resource = 'UserType/'
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
    def people(self):
        cls = getattr(pynetdot.models, 'Person')
        return cls.search(user_type=self.id)


class BaseVlan(n.Netdot):
    """
    A Virtual LAN

    Attributes:
        description: 
        info: 
        name: Human-defined Name for this VLAN
        vid: 
        vlangroup: VLAN group to which this VLAN belongs
        interfaces: List of InterfaceVlan objects
        subnets: List of Ipblock objects
    """
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
    """
    A Virtual LAN Group

    Attributes:
        description: A short description for this VlanGroup
        end_vid: Last VLAN number
        info: 
        name: A name identifying this VLAN group
        start_vid: First VLAN number
        vlans: List of Vlan objects
    """
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
    """
    A DNS Zone

    Attributes:
        active: Whether a DNS zone file should be generated for this Zone
        contactlist: 
        default_ttl: Default TTL to apply to records when exporting the zone file
        expire: A 32 bit time value that specifies the upper limit on the time interval that can elapse before the zone is no longer authoritative.
        export_file: Path and file name to export records to.
        include: Text to include when exporting zone
        info: 
        minimum: The unsigned 32 bit specifying the time to live for negative responses
        mname: The domain-name of the name server that was the original or primary source of data for this zone
        name: The zone or domain name
        refresh: A 32 bit time interval before the zone should be refreshed.
        retry: A 32 bit time interval that should elapse before a failed refresh should be retried.
        rname: A <domain-name> which specifies the mailbox of the person responsible for this zone.
        serial: The unsigned 32 bit version number of the original copy of the zone.  Zone transfers preserve this value.  This value wraps and should be compared using sequence space arithmetic.
        records: List of RR objects
        subnets: List of SubnetZone objects
        aliases: List of ZoneAlias objects
    """
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
    """
    An alias of an existing zone

    Attributes:
        info: 
        name: The zone or domain name
        zone: Zone
    """
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



