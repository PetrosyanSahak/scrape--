import urlparse
import idna
import urllib.parse
from bs4 import BeautifulSoup
import requests
from urllib.parse import quote
from urllib.parse import unquote
from urllib.request import urlopen

url = "https%3A%2F%2F%D5%A1%D5%B6%D5%A4%D6%80%D5%A1%D5%B6%D5%AB%D5%AF.%D5%B0%D5%A1%D5%B5%2F"
url1 = unquote(url)
d = urllib.parse.urlparse(url1)
result = d.scheme + "://" + idna.encode(d.netloc).decode('ascii')
#urlopen(url)
print(result)
#website  = requests.get(result)
website  = urlopen(result)
soup = BeautifulSoup(website, 'html.parser')
print(soup)


class url:
    
    def get_full_url(self):
        if is_absolute(self):
            url_temp = unquote(self.url_m)
            while(url_temp != unquote(url_temp):
                  url_temp = unquote(url_temp)
            d = urllib.parse.urlparse(url1)
            result = d.scheme + "://" + idna.encode(d.netloc).decode('ascii')
            return result
        else:
            
            
      # construct the full url, so that we can open it
      # add scheme and domain if url is relative (https:// + example.com)
      # url unquote if applicable
    def __init__(self, url = '', parent_urls = [], parent_scheme_domain = '', response_code = 0, rss_avail = False):
      url_m = url
      parent_urls_m = parent_urls
      
      parent_scheme_domain_m = parent_scheme_domain # empty if the path is not relative
      response_code_m = response_code
      rss_avail_m = rss_avail
      #is_relative_m = not is_absolute(self) պետք չի առանձին փոփոխական
      
    def is_absolute(self):
        return bool(urlparse.urlparse(self.url_m).netloc)
    
