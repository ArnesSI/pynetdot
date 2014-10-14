import logging
import requests
from simple_cache import SimpleCache
from serializer import *

logger = logging.getLogger(__name__)
cache = SimpleCache.getInstance()

HEADERS = {
    'User_Agent':'python_confgen',
    'Accept':'text/xml; version=1.0',
}
COOKIES_CACHE_KEY = 'netdot_cookie'

def setup(url='http://localhost/netdot/', username='admin', password='password'):
    if not url.endswith('/'):
        url = url + '/'
    Netdot.NETDOT_URL = url
    Netdot.NETDOT_USERNAME = username
    Netdot.NETDOT_PASSWORD = password


    




#def get_xml(obj, search_params, **kwargs):
    #resp = _rest_get(obj, params=search_params)
    #if resp.status_code != requests.codes.ok:
        #if resp.status_code == 404 and 'default' in kwargs:
            #return kwargs['default']
        #resp.raise_for_status()
    #return resp.text

#def get_attr(obj, search_params, attr, **kwargs):
    #txt = get_xml(obj, search_params, **kwargs)
    #value = netodt_deserializer.get_first_attr(txt, attr)
    #return value

def _rest_get(resource, **kwargs):
    url = Netdot.NETDOT_URL + 'rest/' + resource
    response = requests.get(url, cookies=_get_cookies(), headers=HEADERS, **kwargs)
    if response.status_code == 403:
        response = requests.get(url, cookies=_get_cookies(clear_cache=True), headers=HEADERS, **kwargs)
    return response

def _rest_post(resource, params, **kwargs):
    url = Netdot.NETDOT_URL + 'rest/' + resource
    response = requests.post(url, cookies=_get_cookies(), headers=HEADERS, params=params, **kwargs)
    if response.status_code == 403:
        response = requests.post(url, cookies=_get_cookies(clear_cache=True), headers=HEADERS, params=params, **kwargs)
    return response

def _rest_delete(resource, **kwargs):
    url = Netdot.NETDOT_URL + 'rest/' + resource
    response = requests.delete(url, cookies=_get_cookies(), headers=HEADERS, **kwargs)
    if response.status_code == 403:
        response = requests.delete(url, cookies=_get_cookies(clear_cache=True), headers=HEADERS, **kwargs)
    return response

def _get_cookies(clear_cache=False):
    if clear_cache:
        cookies = _login()
        cache.set(COOKIES_CACHE_KEY, cookies)
        return cookies
    else:
        if not cache.get(COOKIES_CACHE_KEY):
            cookies = _login()
            cache.set(COOKIES_CACHE_KEY, cookies)
            return cookies
        else:
            return cache.get(COOKIES_CACHE_KEY)

def _login():
    login_url = Netdot.NETDOT_URL + 'NetdotLogin'
    username = Netdot.NETDOT_USERNAME
    password = Netdot.NETDOT_PASSWORD
    params = {
        'destination':'index.html', 
        'credential_0':username, 
        'credential_1':password, 
        'permanent_session':1,
    }
    response = requests.post(login_url, data=params, headers=HEADERS, allow_redirects=False)
    if response.ok:
        logger.info('Logged into netdot with username %s' % username)
        return response.cookies
    else:
        raise AttributeError('Invalid Credentials')



# -----------------

class Netdot(object):
    global NETDOT_URL, NETDOT_USERNAME, NETDOT_PASSWORD
    NETDOT_URL = 'http://localhost/netdot/'
    NETDOT_USERNAME = 'admin'
    NETDOT_PASSWORD = 'password'

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
        response = _rest_get(cls.resource, params=params)
        if response.status_code == 404:
            return []
        if response.status_code != requests.codes.ok:
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
        response = _rest_get(resource)
        if response.status_code == 404:
            raise Exception('%s with id %d does not existin netdot' % (self.resource, self.id))
        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        self._from_response(response)

    def _from_response(self, response):
        xml = parse_xml(response.text)
        # returns a single tag: <opt id="...
        attrs = xml.attrib
        self._from_netdot(self, attrs)

    @classmethod
    def _from_netdot(cls, obj, attrs):
        """
        Create instance fields from netdots XML response.
        """
        if not isinstance(obj, cls):
            raise Exception('Passed object is not an instance of this class')
        obj._attrs = attrs
        for field in cls._fields:
            field.parse(obj)
        obj.id = attrs['id']
        obj._resolved = True
        obj._original_state = obj._as_dict()

    def _as_dict(self):
        values = dict()
        for f in self._fields:
            values[f.name] = f.raw(getattr(self, f.name))
        return values

    def get_dirty_fields(self):
        new_state = self._as_dict()
        changed_fields = dict([
            (key, value)
            for key, value in self._original_state.iteritems()
            if value != new_state[key]
        ])
        return changed_fields.keys()

    def is_dirty(self):
        if not self.id:
            return True
        return bool(self.get_dirty_fields())

    def display(self, view='all'):
        print '%s:' % self.label
        if view=='all' and not self._views.get(view):
            for f in self._fields:
                value = getattr(self, f.name)
                print "\t%s: %s" % (f.name, value)
        elif self._views.get(view):
            for f_name in self._views.get(view):
                value = getattr(self, f_name)
                print "\t%s: %s" % (f_name, value)
        else:
            raise Exception('View %s not defined' % view)

    def dump(self):
        self.display('all')

    def save(self):
        """
        Save changes to this object back to netdot. Or create a new object if
        id is not set.
        """
        if not self.is_dirty():
            # There were no changes
            return True
        if self.id:
            fields = self.get_dirty_fields()
            resource = '%s%s' % (self.resource, self.id)
        else:
            fields = self._fields
            resource = self.resource
        values = self._as_dict()
        params = {}
        for f in fields:
            params[f.name] = values.get(f.name)
        response = _rest_post(resource, params)
        if response.status_code == 404:
            return False
        if response.status_code != requests.codes.ok:
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
        response = _rest_delete(resource)
        if response.status_code == 404:
            return False
        if response.status_code != requests.codes.ok:
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
