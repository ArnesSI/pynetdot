import xml.etree.ElementTree as ET
from pprint import pprint

def get_first_attr(data, attr):
    # need to encode unicode string to byte string first
    data = data.encode('utf-8')
    root = ET.fromstring(data)
    # xpath attribute searching not supported in python 2.6
    #xpath = './/*[@%s]' % attr
    for e in root.findall('.//*'):
        if e.get(attr):
            return e.get(attr)
    return None

def get_attrs(data, tag_name):
    data = data.encode('utf-8')
    root = ET.fromstring(data)
    results = []
    for tag in root.findall(tag_name):
        results.append(tag.attrib)
    return results
