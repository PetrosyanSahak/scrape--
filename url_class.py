import idna
import urllib.parse
from bs4 import BeautifulSoup
import requests
from urllib.parse import quote
from urllib.parse import unquote
from urllib.request import urlopen


class Url:
    
    def get_full_url(self):
        if self.is_absolute():
            url_temp = self.url_m
        else:
            url_temp = self.parent_scheme_domain_m + self.url_m
            
        while(url_temp != unquote(url_temp)):
              url_temp = unquote(url_temp)

        d = urllib.parse.urlparse(url_temp)
        return d.scheme + "://" + idna.encode(d.netloc).decode('ascii') + quote(d.path)
       # result =  d.scheme + "://" + idna.encode(d.netloc).decode('ascii') + quote(d.path)
       # return result
        

            
      # construct the full url, so that we can open it
      # add scheme and domain if url is relative (https:// + example.com)
      # url unquote if applicable
    def __init__(self, url = '', parent_urls = [], parent_scheme_domain = '', response_code = 0, rss_avail = False):
      self.url_m = url
      self.parent_urls_m = parent_urls
      self.parent_scheme_domain_m = parent_scheme_domain # empty if the path is not relative
      self.response_code_m = response_code
      self.rss_avail_m = rss_avail
      #is_relative_m = not is_absolute(self) պետք չի առանձին փոփոխական
      
    def is_absolute(self):
        return bool(urllib.parse.urlparse(self.url_m).netloc)
    
    
url = "https%3A%2F%2F%D5%A1%D5%B6%D5%A4%D6%80%D5%A1%D5%B6%D5%AB%D5%AF.%D5%B0%D5%A1%D5%B5%2F/գրառում/2023/01/"
#https://անդրանիկ.հայ/գրառում/2023/01/
newurl  = Url(url = url)
print(newurl.get_full_url())
website = urlopen(newurl.get_full_url())
soup = BeautifulSoup(website, "html.parser")
print(soup)
