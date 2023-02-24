# this script is not ready yet
# cannot open aspx websites, even working ones
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import tld
import re

# this line fixes some errors that I did have time to research
# taken form stackoverflow, seems to work
ssl._create_default_https_context = ssl._create_unverified_context

# the only domain we want to scrape
DOMAIN_SCRAPED = "cba.am"
CURSOR_UP = '\033[F'
ERASE_LINE = '\033[K'
SCRAPE_COUNT = 25


urls = ["https://cba.am"]
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
    print(f"{link}\n")
