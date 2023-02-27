import urlparse

class url:
    
    def get_full_url(self):
        if is_absolute(self):
            
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
    
