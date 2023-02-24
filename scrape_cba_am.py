# this script is not ready yet
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 
import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup
import tld
import re

# this line fixes some errors that I did have time to research
# taken form stackoverflow, seems to work
ssl._create_default_https_context = ssl._create_unverified_context

# the only domain we want to scrape
domain_scraped = "cba.am"


#with open('urls.txt') as f:
#  urls = [ line.rstrip() for line in f]

urls = ["https://cba.am"]
visited_urls = set() 
SCRAPE_COUNT = 10
pages_scraped = 0

for url in urls:
    print(f"Current URl being scraped: {url}\n")
    # add the url to the visisted url set
    visited_urls.add(url)
    
    # create a list, which will hold all links in the website
    links = []
    
    try:
        #open the website and get the responce code
        page = urlopen(url)
    except:
        print("!!!!!!!!!!!!!!!!!!!!!!!\n")
        print(f"Could not open url: {url}")
        print("!!!!!!!!!!!!!!!!!!!!!!!\n\n")
        pages_scraped += 1
        continue
    print(f"Responce Code for {url}: {page.getcode()}\n\n")
    
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
        if dom != domain_scraped:
            print(dom)
            continue
        else:
            if(link not in visited_urls):
                print(f"appending link: {link}")
                urls.append(link)
    pages_scraped += 1
    if(pages_scraped > SCRAPE_COUNT):
        break
                     
print("scraping finished, scanned {SCRAPE_COUNT} websites!")
