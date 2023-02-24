# gets the contents of youtube.com and prints it
# in a human readable format (UTF-8)

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://youtube.com"

website = urlopen(url)

soup = BeautifulSoup(website, "html.parser").encode('UTF-8')

print(soup)
