# open youtube.com and print the responce code

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://youtube.com"

website = urlopen(url)
print(f"{url} responce code: {website.getcode()}")


