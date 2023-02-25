# check if there is an RSS feed
# check all links in the html, if there is a link
# of type application/rss+xml then that link has RSS feed
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = "https://www.schneier.com/"

page = urlopen(url)
# print(page.getcode())

soup = BeautifulSoup(page, "html.parser")

for link in soup.find_all(attrs={'href': re.compile("http")}):
  if link.get('type') == "application/rss+xml":
      print(f"RSS feed available for {link}")
  
