# gets the tld of the url
# this is useful, because we want to limit the
# urls only to urls with .am tlds
# to work requires tld to be imported
# if it is not installed on your machine install it with
# pip install tld

from tld import get_tld

url = "https://www.youtube.com/watch?v=cE72CpmIcFk"
print(get_tld(url)) # should print "com"

url = "https://www.cba.am/am/SitePages/mpobjective.aspx"
print(get_tld(url)) # should print "am"
