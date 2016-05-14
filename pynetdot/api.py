import requests
import logging

logger = logging.getLogger(__name__)


class NetdotAPI(object):
    HEADERS = {
        'User_Agent':'python_confgen',
        'Accept':'text/xml; version=1.0',
    }

    def __init__(self, url='http://localhost/netdot/', username='admin', password='password'):
        if not url.endswith('/'):
            url = '%s/' % url
        self.url = url
        self.username = username
        self.password = password
        self._cookies = None

    def get(self, resource, **kwargs):
        url = self.url + 'rest/' + resource
        response = requests.get(url, cookies=self._get_cookies(), headers=self.HEADERS, **kwargs)
        if response.status_code == 403:
            response = requests.get(url, cookies=self._get_cookies(clear_cache=True), headers=self.HEADERS, **kwargs)
        return response

    def post(self, resource, params, **kwargs):
        url = self.url + 'rest/' + resource
        response = requests.post(url, cookies=self._get_cookies(), headers=self.HEADERS, params=params, **kwargs)
        if response.status_code == 403:
            response = requests.post(url, cookies=self._get_cookies(clear_cache=True), headers=self.HEADERS, params=params, **kwargs)
        return response

    def delete(self, resource, **kwargs):
        url = self.url + 'rest/' + resource
        response = requests.delete(url, cookies=self._get_cookies(), headers=self.HEADERS, **kwargs)
        if response.status_code == 403:
            response = requests.delete(url, cookies=self._get_cookies(clear_cache=True), headers=self.HEADERS, **kwargs)
        return response

    def _get_cookies(self, clear_cache=False):
        if clear_cache:
            self._cookies = self._login()
            return self._cookies
        else:
            if not self._cookies:
                self._cookies = self._login()
                return self._cookies
            else:
                return self._cookies

    def _login(self):
        login_url = self.url + 'NetdotLogin'
        username = self.username
        password = self.password
        params = {
            'destination':'index.html',
            'credential_0':username,
            'credential_1':password,
            'permanent_session':1,
        }
        response = requests.post(login_url, data=params, headers=self.HEADERS, allow_redirects=False)
        if response.ok:
            logger.info('Logged into netdot with username %s' % username)
            return response.cookies
        else:
            raise AttributeError('Invalid Credentials')
