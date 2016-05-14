import pynetdot.models
from dateutil import parser as datetime_parser
from datetime import datetime, date

class BaseField(object):
    def __init__(self, name, **kwargs):
        if not name:
            raise Exception('Need to specify name')
        self.name = name
        self.default = kwargs.pop('default', None)
        self.display_name = kwargs.pop('display_name', name)

    def serialize(self, obj):
        value = getattr(obj, self.name)
        if value is None:
            return ''
        elif value == False:
            return '0'
        elif value == True:
            return '1'
        else:
            return str(value)

    def parse(self, obj):
        value = obj._attrs.get(self.name, self.default)
        value = self._clean(value)
        setattr(obj, self.name, value)

    def raw(self, v):
        return v

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

    def raw(self, v):
        if v == True:
            return '1'
        elif v == False:
            return '0'
        return v

class DateField(BaseField):
    def _clean(self, v):
        if not v or v == '':
            return None
        date = datetime_parser.parse(v)
        return date.date()

    # TODO serialize

    def raw(self, v):
        if (isinstance(v, date)):
            return v.strftime('%Y-%m-%d')
        elif not v:
            return ''
        return v

class DateTimeField(BaseField):
    def _clean(self, v):
        if not v or v == '':
            return None
        try:
            date = datetime_parser.parse(v, dayfirst=True)
        except:
            return None
        if date.year == 1970:
            # if there is no timestamp the field will contain:
            # '1970-01-02 00:00:01'
            # yes, this is a bit of a hack
            return None
        return date

    # TODO serialize

    def raw(self, v):
        if (isinstance(v, datetime)):
            return v.strftime('%Y-%m-%d %H:%M:%S')
        elif not v:
            return ''
        return v

class StringField(BaseField):
    def __init__(self, name, **kwargs):
        default = kwargs.get('default', '')
        if not default:
            default = ''
        default = str(default)
        kwargs['default'] = default
        super(StringField, self).__init__(name, **kwargs)

    def raw(self, v):
        if not v:
            return ''
        return v

class LinkField(BaseField):
    def __init__(self, name, **kwargs):
        self.link_to = kwargs.pop('link_to')
        super(LinkField, self).__init__(name, **kwargs)

    def serialize(self, obj):
        value = getattr(obj, self.name)
        if hasattr(value, 'id'):
            return str(value.id)
        else:
            try:
                int(value)
            except TypeError, ValueError:
                return ''
            else:
                return str(value)

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

    def raw(self, v):
        if hasattr(v, 'id'):
            return int(v.id)
        elif not v:
            return None
        return int(v)
