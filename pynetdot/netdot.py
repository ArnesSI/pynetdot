import logging
from serializer import parse_xml
from api import NetdotAPI

logger = logging.getLogger(__name__)
api = None

def setup(url='http://localhost/netdot/', username='admin', password='password'):
    global api
    api = NetdotAPI(url=url, username=username, password=password)


class Netdot(object):

    resource = None

    def __init__(self, **kwargs):
        self._resolved = False
        self.id = kwargs.get('id', None)
        self._attrs = {}
        self._original_state = {}
        if not self.id:
            # create a new empty instance with default field values
            # there will be nothing to resolve so no point in trying
            self._resolved = True
            for field in self._fields:
                setattr(self, field.name, field.default)

    @classmethod
    def _build_search_params(cls, **kwargs):
        for k,v in kwargs.items():
            if isinstance(v, Netdot):
                kwargs[k] = str(v.id)
        return kwargs

    @classmethod
    def all(cls):
        return cls._search()

    @classmethod
    def search(cls, **kwargs):
        if not kwargs:
            raise Exception('Need to specify search parameters')
        return cls._search(**kwargs)

    @classmethod
    def _search(cls, **kwargs):
        params = cls._build_search_params(**kwargs)
        response = api.get(cls.resource, params=params)
        if response.status_code == 404:
            return []
        if not response.ok:
            response.raise_for_status()
        xml = parse_xml(response.text)
        results = []
        for c in xml:
            obj = cls(id=c.attrib['id'])
            cls._from_netdot(obj, c.attrib)
            results.append(obj)
        return results

    @classmethod
    def get_first(cls, **kwargs):
        results = cls.search(**kwargs)
        if not results:
            return None
        return results[0]

    @classmethod
    def get(cls, id):
        obj = cls(id=id)
        obj._resolve()
        return obj

    def _resolve(self):
        """
        GET object attributes for this object (by its id) and set its fields.
        """
        logger.debug('Resolving %s ID:%d' % (self.__class__, self.id))
        if not self.id:
            raise Exception('id not set')
        resource = '%s%s' % (self.resource, self.id)
        response = api.get(resource)
        if response.status_code == 404:
            raise Exception('%s with id %d does not exist in netdot' % (self.resource, self.id))
        if not response.ok:
            response.raise_for_status()
        self._from_response(response)

    def _from_response(self, response):
        xml = parse_xml(response.text)
        # returns a single tag: <opt id="...
        attrs = xml.attrib
        self._from_netdot(self, attrs)

    @classmethod
    def _from_netdot(cls, obj, attrs):
        '''
        Create instance fields from netdot's XML response.
        '''
        if not isinstance(obj, cls):
            raise Exception('Passed object is not an instance of this class')
        obj._attrs = attrs
        for field in cls._fields:
            field.parse(obj)
        obj.id = int(attrs['id'])
        obj._resolved = True
        obj._original_state = obj._as_dict()

    def _as_dict(self):
        values = dict()
        for f in self._fields:
            values[f.name] = f.raw(getattr(self, f.name))
        return values

    def get_dirty_fields(self):
        '''
        Return a list of fields that have been modified.
        '''
        new_state = self._as_dict()
        changed_fields = dict([
            (key, value)
            for key, value in self._original_state.iteritems()
            if value != new_state[key]
        ])
        return changed_fields.keys()

    def is_dirty(self):
        '''
        Returns True if object was modified.
        '''
        if not self.id:
            return True
        return bool(self.get_dirty_fields())

    def display(self, view='all'):
        '''
        Returns a string displaying the object attributes for the given view.
        '''
        ds = u'%s:\n' % self.label
        if view=='all' and not self._views.get(view):
            for f in self._fields:
                value = getattr(self, f.name)
                ds += u'\t%s: %s\n' % (f.name, value)
        elif self._views.get(view):
            for f_name in self._views.get(view):
                value = getattr(self, f_name)
                ds += u'\t%s: %s\n' % (f_name, value)
        else:
            raise Exception('View %s not defined' % view)
        return ds

    def dump(self):
        '''
        Returns a string displaying all attribures of the object.
        '''
        return self.display('all')

    def save(self):
        """
        Save changes to this object back to netdot. Or create a new object if
        id is not set.
        """
        if not self.is_dirty():
            # There were no changes
            return True
        if self.id:
            field_names = self.get_dirty_fields()
            fields = []
            for fn in field_names:
                for f in self._fields:
                    if f.name == fn:
                        fields.append(f)
            resource = '%s%s' % (self.resource, self.id)
        else:
            fields = self._fields
            resource = self.resource
        values = self._as_dict()
        params = {}
        for f in fields:
            value_serialized = f.serialize(self)
            params[f.name] = value_serialized
        response = api.post(resource, params)
        if response.status_code == 404:
            return False
        if not response.ok:
            response.raise_for_status()
        # Reset all values from server response
        self._from_response(response)
        # Reset initial field values
        self._original_state = self._as_dict()
        return True

    def delete(self):
        """
        Delete object from netdot database.
        """
        if not self.id:
            # no id means this object was not created in netdot yet
            return True
        resource = '%s%s' % (self.resource, self.id)
        response = api.delete(resource)
        if response.status_code == 404:
            return False
        if not response.ok:
            response.raise_for_status()
        # Unset id so saving this instance again will create a new object in netdot DB
        self.id = None
        return True

    def __getattr__(self, attr, default=None):
        """
        Unresolved instances do not have their attributes set yet. Resolve the
        object before trying to get its attribute.
        """
        if not self._resolved:
            self._resolve()
        try:
            return self.__dict__[attr]
        except KeyError as e:
            if default:
                return default
            raise AttributeError("%r object has no attribute %r" % (self.__class__, attr))

    def __unicode__(self):
        return self.label

    def __str__(self):
        u = unicode(self)
        return u.encode('utf-8', 'replace')

    def __repr__(self):
        if not self.id:
            return '%s.%s()' % (self.__class__.__module__, self.__class__.__name__)
        else:
            return '%s.%s("%s")' % (self.__class__.__module__, self.__class__.__name__, self.label)
