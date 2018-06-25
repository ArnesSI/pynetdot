import warnings
import xml.etree.ElementTree as ET

# string below is:
# ''.join([chr(i) for i in range(9)+[11,12]+range(14,32)])
INVALID_CHARS = '\x00\x01\x02\x03\x04\x05\x06\x07\x08\x0b\x0c\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f'
INVALID_CHARS_DICT = {ord(c): None for c in INVALID_CHARS}


def parse_xml(data):
    if type(data) is not str:
        # on python3 response will be bytes() and needs to be decoded as utf-8
        data = data.decode('utf-8')
    data = _xml_pre_clean(data)
    root = ET.fromstring(data)
    return root

def _xml_pre_clean(data):
    # i've seen cases wher netdot sends invalid chars in xml response
    # these were mostly control chars in dp_remote_port in Interface endpoint
    # this chars make for invalid xml and xml parsers bail at that point
    # https://www.w3.org/TR/xml/#charsets
    # the data sent out should really be sanitized in netdot
    # but until it is, we still want pynetdot to not crash
    # so, i'll strip out some invalid chars and hope for the best
    # also throw a warning at user
    if any(c in data for c in INVALID_CHARS):
        warnings.warn('One or more invalid characters found in XML string received from netdot API. They were removed. Unpredictable side effects possible.')
        return data.translate(INVALID_CHARS_DICT)
    else:
        return data
