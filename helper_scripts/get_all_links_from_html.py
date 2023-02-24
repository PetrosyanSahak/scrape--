# open youtube.com, print the responce code
# find all links in the html
# print found links
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = "https://youtube.com"

page = urlopen(url)
print(page.getcode())

soup = BeautifulSoup(page, "html.parser")
links = []

for link in soup.find_all(attrs={'href': re.compile("http")}):
    links.append(link.get('href'))
  
for link in links:
  print(link)
  
