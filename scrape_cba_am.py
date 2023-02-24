# this script is not ready yet
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import tld
import re

domain_scraped = "cba.am"
with open('urls.txt') as f:
  urls = [ line.rstrip() for line in f]

visited_urls = {}

pages_scraped = 0

for url in urls:
    # add the url to the visisted url set
    visited_urls += url
    
    # create a list, which will hold all links in the website
    links = []
    
    #open the website and get the responce code
    page = urlopen(url)
    print(f"Responce Code for {url}: {page.getcode}\n")
    
    # find all links in the current url, and add it to the links list
    soup = BeautifulSoup(page, "html.parser")
    for link in soup.find_all(attrs={'href': re.compile("http")}):
        links.append(link.get('href')
     
    # check if the link's domain is cba.am
    # and we have not visited it, add it to the queue
    for link in links:
        # get domain.tld of the current url
        res = tld.get_tld(link, as_object=True)
        dom = f"{res.domain}.{res}"
        #if the domain.tld is not cba.am continue
        if dom != "cba.am":
            continue
        else
            if(link not in visited_urls):
                     url += link
    pages_scraped += 1
    if(pages_scraped > 1000):
        break
                     
print("scraping finished, scanned 1000 websites!")
