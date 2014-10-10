#!/usr/bin/env python

import sys
from pprint import pprint
from warnings import warn
from xml.etree import ElementTree as ET
import pynetdot
from pynetdot.fields import *

resources = [
    #'accessright',
    'arpcache',
    'arpcacheentry',
    'asset',
    #'audit',
    'availability',
    'bgppeering',
    'backbonecable',
    'cablestrand',
    'cabletype',
    'circuit',
    'circuitstatus',
    'circuittype',
    'closet',
    #'closetpicture',
    'contact',
    'contactlist',
    'contacttype',
    #'datacache',
    'device',
    'deviceattr',
    'deviceattrname',
    'devicecontacts',
    'devicemodule',
    'dhcpattr',
    'dhcpattrname',
    'dhcpscope',
    'dhcpscopetype',
    'dhcpscopeuse',
    'entity',
    'entityrole',
    'entitysite',
    'entitytype',
    'fwtable',
    'fwtableentry',
    'fibertype',
    'floor',
    #'floorpicture',
    'groupright',
    'horizontalcable',
    'hostaudit',
    'interface',
    'interfacevlan',
    'ipservice',
    'ipblock',
    'ipblockattr',
    'ipblockattrname',
    'ipblockstatus',
    'maintcontract',
    'monitorstatus',
    'oui',
    'person',
    'physaddr',
    'physaddrattr',
    'physaddrattrname',
    'product',
    'producttype',
    'rr',
    'rraddr',
    'rrcname',
    'rrds',
    'rrhinfo',
    'rrloc',
    'rrmx',
    'rrnaptr',
    'rrns',
    'rrptr',
    'rrsrv',
    'rrtxt',
    'room',
    'stpinstance',
    #'savedqueries',
    #'schemainfo',
    'service',
    'site',
    'sitelink',
    #'sitepicture',
    'sitesubnet',
    'splice',
    'strandstatus',
    'subnetzone',
    #'userright',
    #'usertype',
    'vlan',
    'vlangroup',
    'zone',
    'zonealias',
    #'backbonecable_history',
    #'cablestrand_history',
    #'circuit_history',
    #'contact_history',
    #'device_history',
    #'entity_history',
    #'interface_history',
    #'person_history',
    #'product_history',
    #'site_history',
    #'sitelink_history',
    #'vlangroup_history',
]

#resources = ['entity']

supported_types = {
     'bigint': 'IntegerField',
     'bool': 'BoolField',
     'date': 'DateField',
     'integer': 'IntegerField',
     #'longblob': NOT supported
     'numeric': 'StringField', # FIXME this is used for ip addresses which are rendered as strings by netdot REST
     'text': 'StringField',
     'timestamp': 'DateTimeField',
     'varchar': 'StringField',
}

models = {}
reverse_links = {}

for r in resources:
    resp = pynetdot.netdot._rest_get('%s/meta_data' % r)
    xml = ET.fromstring(resp.text)
    model = {}
    model['resource'] = xml.attrib['name']
    model['class_name'] = model['resource']
    model['id_field'] = xml.attrib['primary_key']
    fields = []

    # column tags
    for c in xml.findall('columns'):
        f_class = ''
        f_args = ''
        f_name = c.attrib['id']
        f_reverse = ''
        c_type = c.attrib.get('type', '')
        c_tag = c.attrib.get('tag', f_name)
        f_args += ', display_name=\'%s\'' % c_tag
        for c_child in c:
            # check of linksto child tags and configure a link field
            if c_child.tag == 'linksto':
                f_class = 'LinkField'
                f_args += ', link_to=\'%s\'' % c_child.attrib['table']
                link_target = reverse_links.get(c_child.attrib['table'], [])
                f_reverse = c_child.attrib.get('method', None)
                if f_reverse:
                    reverse_def = {
                        'method': f_reverse,
                        'target': model['resource'],
                        'field': f_name
                    }
                    link_target.append(reverse_def)
                    reverse_links[c_child.attrib['table']] = link_target
        if not f_class:
            # this is a regular field
            f_class = supported_types.get(c_type)
        # skip id_fields
        if f_name == model['id_field']:
            continue
        if not f_class:
            warn('Usupported column type: %s %s %s' % (class_name, f_name, c_type))
            continue
        fields.append({'class':f_class, 'name':f_name, 'args':f_args})
    model['fields'] = fields

    # label tag
    model['label'] = []
    for c in xml.findall('label'):
        model['label'].append(c.text)

    # views
    views = {}
    views_element = xml.find('views')
    for c in views_element:
        view = views.get(c.tag, [])
        view.append(c.text)
        views[c.tag] = view
    model['views'] = views

    models[model['resource']] = model
    #break
    
#pprint(models)
#sys.exit(1)

# print results
print '''import pynetdot.netdot as n
import pynetdot.fields as f
import pynetdot.models
'''

from jinja2 import Environment, FileSystemLoader
env = Environment(
    loader=FileSystemLoader('/home/nms/tmp/matej/pynetdot/'),
    trim_blocks=True,
    lstrip_blocks=True
)
template = env.get_template('BaseModel.tmpl')
print template.render(models=models, reverse_links=reverse_links)
