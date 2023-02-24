# this script gets the 'main' domain with the tld (without any subdomain)
# we have certain domains that we should not scan
# so we will check if the url belongs to the restricted domains

from urllib.parse import urlparse
import tld

url = "https://www.youtube.com/watch?v=cE72CpmIcFk"
res = tld.get_tld(url, as_object=True)
print(f"{res.domain}.{res}") # should print "youtube.com"

url = "https://www.cba.am/am/SitePages/mpobjective.aspx"
res = tld.get_tld(url, as_object=True)
print(f"{res.domain}.{res}") # should print "cba.am"
