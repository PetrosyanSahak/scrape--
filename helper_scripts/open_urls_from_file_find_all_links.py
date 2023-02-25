# requires urls.txt to be present
# opens every url in the urls.txt file
# finds all the links in each url
# prints all the found links
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import ssl
import re

ssl._create_default_https_context = ssl._create_unverified_context
with open('urls.txt') as f:
  urls = [ line.rstrip() for line in f]
  
links = []
for url in urls:
    try:
        page = urlopen(url)
    except HTTPError as err:
        response = err.code
        print(f"RESPONSE CODE:    {response}")
        print(f"could not open website {url}. HTTPError")
        continue
    except URLError as err:
        print(f"could not open website {url}. URLError")
        continue
    except:
        print(f"could not open website {url}. EXCEPT")
        continue
    print(f"Response Code for {url}: {page.getcode()}\n")
  
    soup = BeautifulSoup(page, "html.parser")
    for link in soup.find_all(attrs={'href': re.compile("http")}):
        links.append(link.get('href'))

for link in links:
    print(link)
