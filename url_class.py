import argparse as ap
import idna
import urllib.parse
from urllib.parse import quote
from urllib.parse import unquote
from urllib.request import urlopen


class Url:
    def get_full_url(self):
        if self.is_absolute():
            url_temp = self.url_m
        else:
            url_temp = self.parent_scheme_domain_m + self.url_m

        while url_temp != unquote(url_temp):
            url_temp = unquote(url_temp)

        d = urllib.parse.urlparse(url_temp)
        return d.scheme + "://" + idna.encode(d.netloc).decode('ascii') + quote(d.path)

    def __init__(self, url_, parent_urls=[], parent_scheme_domain='',
                 response_code=0, rss_avail=False):
        self.url_m = url_
        self.parent_urls_m = parent_urls
        self.parent_scheme_domain_m = parent_scheme_domain  # empty if the path is not relative
        self.response_code_m = response_code
        self.rss_avail_m = rss_avail

    def is_absolute(self):
        return bool(urllib.parse.urlparse(self.url_m).netloc)


parser = ap.ArgumentParser(description="get any url, return it in utf-8")
parser.add_argument('url')
args = parser.parse_args()
url = args.url
# url = "https%3A%2F%2F%D5%A1%D5%B6%D5%A4%D6%80%D5%A1%D5%B6%D5%AB%D5%AF.%D5%B0%D5%A1%D5%B5%2F/գրառում/2023/01/"
# https://անդրանիկ.հայ/գրառում/2023/01/
newUrl = Url(url)
print(newUrl.get_full_url())
website = urlopen(newUrl.get_full_url())
print(website.getcode())
