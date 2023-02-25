# this script is not ready yet
# some websites cannot be opened, even though 
# with browser it opens
# scan number is 25, but returns only 17 url. Must be some bug
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import ssl
import tld
import re

# this line fixes some errors that I did not have time to research
# taken from stackoverflow, seems to work
ssl._create_default_https_context = ssl._create_unverified_context
with open('restricted_domains.txt') as f:
  RESTRICTED_DOMAINS = { line.rstrip() for line in f}

with open('urls.txt') as f:
  urls = [ line.rstrip() for line in f]


# the only domain we want to scrape
DOMAIN_SCRAPED = "cba.am"
CURSOR_UP = '\033[F'
ERASE_LINE = '\033[K'
SCRAPE_COUNT = 25

print("Starting urls to be scanned!\n")
for link in urls:
    print(link)

print()

url_could_not_open = set()
url_1xx_response = set()
url_2xx_response = set()
url_3xx_response = set()
url_4xx_response = set()
url_5xx_response = set()
visited_urls = set() 

pages_scraped = 0
print()
for url in urls:
    if(pages_scraped > SCRAPE_COUNT):
        break
    
    res = tld.get_tld(url, as_object=True)
    dom = f"{res.domain}.{res}"
    # print(dom)
    if dom in RESTRICTED_DOMAINS:
        print(f"Restricted domain encountered {dom}, continuing...")
        continue
    #if the domain.tld is not cba.am continue
    if dom != DOMAIN_SCRAPED:
        # print(dom)
        continue

    print(CURSOR_UP + ERASE_LINE + CURSOR_UP)
    print(f"{pages_scraped} out of {SCRAPE_COUNT} have been scraped...")
    # add the url to the visisted url set
    visited_urls.add(url)
    
    # create a list, which will hold all links in the website
    links = []
    
    try:
        #open the website and get the responce code
        page = urlopen(url)
    except:
        # print("!!!!!!!!!!!!!!!!!!!!!!!\n")
        # print(f"Could not open url: {url}")
        # print("!!!!!!!!!!!!!!!!!!!!!!!\n\n")
        pages_scraped += 1
        url_could_not_open.add(url)
        continue

    response = page.getcode()
    # print(f"Response Code for {url}: {response}\n\n")

    if 100 <= response < 200:
        url_1xx_response.add(url)
    elif 200 <= response < 300:
        url_2xx_response.add(url)
    elif 300 <= response < 400:
        url_3xx_response.add(url)
    elif 400 <= response < 500:
        url_4xx_response.add(url)
    elif 500 <= response < 600:
        url_2xx_response.add(url)
    
    # find all links in the current url, and add it to the links list
    soup = BeautifulSoup(page, "html.parser")
    for link in soup.find_all(attrs={'href': re.compile("http")}):
        links.append(link.get('href'))
     
    # check if the link's domain is cba.am
    # and we have not visited it, add it to the queue
    for link in links:
        # get domain.tld of the current url
        res = tld.get_tld(link, as_object=True)
        dom = f"{res.domain}.{res}"
        #if the domain.tld is not cba.am continue
        if dom != DOMAIN_SCRAPED:
            # print(dom)
            continue
        elif dom in RESTRICTED_DOMAINS:
            print(f"Encountered restricted domain {link}, continue...")
            continue
        else:
            if(link not in visited_urls):
                # print(f"appending link: {link}")
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

data = { '1xx':len(url_1xx_response),
        '2xx':len(url_2xx_response), 
        '3xx':len(url_3xx_response), 
        '4xx':len(url_4xx_response), 
        '5xx':len(url_5xx_response), 
        'Could not open':len(url_could_not_open) }

response_type = list(data.keys())
response_count = list(data.values())

fig = plt.figure(figsize = (10, 5))

plt.bar(response_type, response_count, color='maroon', width = 0.4)

plt.xlabel("Return codes (optionally could not open)")
plt.ylabel("No. of websites")

plt.title("Website response codes")
plt.show()
