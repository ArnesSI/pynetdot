import xml.etree.ElementTree as ET
from pprint import pprint

def parse_xml(data):
    # need to encode unicode string to byte string first
    data = data.encode('utf-8')
    root = ET.fromstring(data)
    return root
