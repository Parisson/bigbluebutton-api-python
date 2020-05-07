
from hashlib import sha1
from re import match
import urllib

class UrlBuilder:
    def __init__(self, bbbServerBaseUrl, securitySalt):
        if not match('/[http|https]:\/\/[a-zA-Z1-9.]*\/bigbluebutton\/api\//', bbbServerBaseUrl):
            if not bbbServerBaseUrl.startswith("http://") and not bbbServerBaseUrl.startswith("https://"):
                bbbServerBaseUrl = "http://" + bbbServerBaseUrl
            if not bbbServerBaseUrl.endswith("/bigbluebutton/api/"):
                bbbServerBaseUrl = bbbServerBaseUrl[:(bbbServerBaseUrl.find("/", 8)
                    if bbbServerBaseUrl.find("/", 8) != -1 else len(bbbServerBaseUrl))] + "/bigbluebutton/api/"

        self.securitySalt         = securitySalt
        self.bbbServerBaseUrl     = bbbServerBaseUrl

    def buildQueryString(self, params):
        sanitazed = {}
        for key, value in params.items():
            if value is None:
                continue
            if isinstance(value, bool):
                value = "true" if value else "false"
            else:
                try:
                    value = str(value)
                except UnicodeEncodeError:
                    value = value.encode('utf-8')
            sanitazed[key] = value
        return urllib.urlencode(sanitazed)

    def buildUrl(self, api_call, params={}):
        url = self.bbbServerBaseUrl
        url += api_call + "?"
        url += self.buildQueryString(params)
        url += "&checksum=" + self.__get_checksum(api_call, params)
        return url

    def __get_checksum(self, api_call, params={}):
        secret_str = api_call
        secret_str += self.buildQueryString(params)        
        secret_str += self.securitySalt
        return sha1(secret_str).hexdigest()
