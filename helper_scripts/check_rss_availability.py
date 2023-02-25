from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re

urls = [
    "https://www.schneier.com/",
    "https://www.list.am/",
    "https://www.antranigv.am/weblog/",
]
for url in urls:
    try:
        page = urlopen(url)
    except HTTPError as err:
        print(f"could not open website {url}. HTTPError")
        print(err.code)
        continue
    except URLError as err:
        print(f"could not open website {url}. URLError")
        continue

    print(page.getcode())

    soup = BeautifulSoup(page, "html.parser")
    links = []

    for link in soup.find_all(attrs={"href": re.compile("http")}):
        links.append(link.get("href"))
        if link.get("type") == "application/rss+xml":
            print(f"RSS available for {link.get('href')}")
