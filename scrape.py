import idna
import validators
import urllib.parse
from urllib.parse import unquote
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import ssl
import tld
import re

def idnencode(url, current_domain=""):
    url = unquote(url)
    if(not validators.url(url)):
        url = "http://" + current_domain + url 
    try:
        d = urllib.parse.urlparse(url)
        return d.scheme + "://" + idna.encode(d.netloc).decode('ascii') + d.path
    except:
        print(url)
        exit(1)

def add_url_to_set(response, url):
        if 100 <= response < 200:
            url_1xx_response.append(url)
        elif 200 <= response < 300:
            url_2xx_response.append(url)
        elif 300 <= response < 400:
            url_3xx_response.append(url)
        elif 400 <= response < 500:
            url_4xx_response.append(url)
        elif 500 <= response < 600:
            url_5xx_response.append(url)

ssl._create_default_https_context = ssl._create_unverified_context

with open("restricted_domains.txt") as f:
    RESTRICTED_DOMAINS = {line.rstrip() for line in f}

with open("urls.txt") as f:
    urls = [idnencode(line.rstrip()) for line in f]


# the only domain we want to scrape
# DOMAINS_SCRAPED = ["lichess.org", "cba.am"]
CURSOR_UP = "\033[F"
ERASE_LINE = "\033[K"
SCRAPE_COUNT = 25
pages_scraped = 0

print("Starting urls to be scanned!\n")
for link in urls:
    print(link)
print()
url_could_not_open = [] 
url_1xx_response = []
url_2xx_response = []
url_3xx_response = []
url_4xx_response = []
url_5xx_response = []
visited_urls = set()

for url in urls:
    if pages_scraped > SCRAPE_COUNT:
        break

    res = tld.get_tld(url, as_object=True)
    dom = f"{res.domain}.{res}"

    if dom in RESTRICTED_DOMAINS:
        print(f"Restricted domain encountered {dom}, continuing...")
        continue

    # if the domain.tld is not cba.am continue
    # if dom not in DOMAINS_SCRAPED:
    #     print(dom)
    #     continue

    print(CURSOR_UP + ERASE_LINE + CURSOR_UP)
    print(f"{pages_scraped} out of {SCRAPE_COUNT} have been scraped...")
    # add the url to the visisted url set
    visited_urls.add(url)

    # create a list, which will hold all links in the website
    links = []

    try:
        page = urlopen(url)
    except HTTPError as err:
        add_url_to_set(err.code, url)
        print(f"could not open website {url}. HTTPError")
        continue
    except URLError as err:
        print(f"could not open website {url}. URLError")
        url_could_not_open.append(url)
        continue
    except:
        print(f"could not open website {url}. EXCEPT")
        url_could_not_open.append(url)
        continue

    response = page.getcode()
    add_url_to_set(page.getcode(), url)

    # find all links in the current url, and add it to the links list
    soup = BeautifulSoup(page, "html.parser")
    for link in soup.find_all(attrs={"href": re.compile("http")}):
        links.append( idnencode(link.get("href"), dom))

    for link in soup.find_all(attrs={"xlink:href": re.compile("http")}):
        links.append( idnencode(link.get("xlink:href"), dom))

    # if we have not visited the link, add it to the list
    for link in links:
        # get domain.tld of the current url
        try:
            res = tld.get_tld(link, as_object=True)
            dom = f"{res.domain}.{res}"
        except:
            print(f"not a valid url {link}")
            
            continue
        # if the domain.tld is not cba.am continue
        # if dom not in DOMAINS_SCRAPED:
        #     print(dom)
        #     continue
        if dom in RESTRICTED_DOMAINS:
            print(f"Encountered restricted domain {link}, continue...")
            continue
        if link not in visited_urls:
            urls.append(link)
    pages_scraped += 1

print(f"scraping finished, scanned {SCRAPE_COUNT} websites!")

print("Webistes which response value starts with 1xx\n")
for link in url_1xx_response:
    print(f"{link}\n")

print("\n\n")

print("Webistes which response value starts with 2xx\n")
for link in url_2xx_response:
    print(f"{link}\n")

print("\n\n")

print("Webistes which response value starts with 3xx\n")
for link in url_3xx_response:
    print(f"{link}\n")

print("\n\n")
print("Webistes which response value starts with 4xx\n")
for link in url_4xx_response:
    print(f"{link}\n")

print("\n\n")

print("Webistes which response value starts with 5xx\n")
for link in url_5xx_response:
    print(f"{link}\n")

print("\n\n")


print("ATTENTION, WE COULD NOT OPEN THESE WEBSITES!!!\n")
for link in url_could_not_open:
    print(f"{link}")

print()
print("urls visited with 2xx response")
print()
for link in url_2xx_response:
    print(f"{link}")
data = {
    "1xx": len(url_1xx_response),
    "2xx": len(url_2xx_response),
    "3xx": len(url_3xx_response),
    "4xx": len(url_4xx_response),
    "5xx": len(url_5xx_response),
    "Could not open": len(url_could_not_open),
}

print("--------------------")

response_type = list(data.keys())
response_count = list(data.values())

fig = plt.figure(figsize=(10, 5))

plt.bar(response_type, response_count, color="maroon", width=0.4)

plt.xlabel("Return codes (optionally could not open)")
plt.ylabel("No. of websites")

plt.title("Website response codes")
plt.show()
