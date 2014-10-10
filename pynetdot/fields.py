import pynetdot.models
from dateutil import parser as datetime_parser

class BaseField(object):
    def __init__(self, name, **kwargs):
        if not name:
            raise Exception('Need to specify name')
        self.name = name
        self.default = kwargs.pop('default', None)
        self.display_name = kwargs.pop('display_name', name)

    def parse(self, obj):
        value = obj._attrs.get(self.name, self.default)
        value = self._clean(value)
        setattr(obj, self.name, value)

    def _clean(self, v):
        return v

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.name)


class IntegerField(BaseField):
    def _clean(self, v):
        if v == '':
            return None
        return int(v)


class BoolField(BaseField):
    def _clean(self, v):
        if v == '0':
            return False
        return bool(v)


class DateField(BaseField):
    def _clean(self, v):
        if not v or v == '':
            return None
        date = datetime_parser.parse(v)
        return date.date()


class DateTimeField(BaseField):
    def _clean(self, v):
        if not v or v == '':
            return None
        date = datetime_parser.parse(v, dayfirst=True)
        if date.year == 1970:
            # if there is no timestamp the field will contain:
            # '1970-01-02 00:00:01'
            # yes, this is a bit of a hack
            return None
        return date


class StringField(BaseField):
    def __init__(self, name, **kwargs):
        default = kwargs.get('default', '')
        if not default:
            default = ''
        default = str(default)
        kwargs['default'] = default
        super(StringField, self).__init__(name, **kwargs)


class LinkField(BaseField):
    def __init__(self, name, **kwargs):
        self.link_to = kwargs.pop('link_to')
        super(LinkField, self).__init__(name, **kwargs)

    def parse(self, obj):
        xlink = '%s_xlink' % self.name
        link = obj._attrs.get(xlink, None)
        if not link:
            setattr(obj, self.name, None)
            return None
        link_id = int(link.replace('%s/' % self.link_to, ''))
        class_ = getattr(pynetdot.models, self.link_to)
        linked_obj = class_(id=link_id)
        setattr(obj, self.name, linked_obj)
