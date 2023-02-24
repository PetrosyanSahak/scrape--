# requires urls.txt to be present
# opens every url in the urls.txt file
# finds all the links in each url
# prints all the found links
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

with open('urls.txt') as f:
  urls = [ line.rstrip() for line in f]
  
links = []
for url in urls:
    page = urlopen(url)
    print(f"Responce Code for {url}: {page.getcode}\n")
  
    soup = BeautifulSoup(page, "html.parser")
    for link in soup.find_all(attrs={'href': re.compile("http")}):
        links.append(link.get('href')
          
for link in links:
    print(link)
