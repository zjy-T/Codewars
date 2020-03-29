# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
from tldextract import extract
from urllib.parse import urlparse
import re
url = "http://google.com"

def domain_name(url):
    if urlparse(url).netloc == "":
        t = urlparse(url).path
        holder = t.split(".")
        if holder[0] == "www":
            return holder[1]
        else:
            return holder[0]
    else:
        t = urlparse(url).netloc
        holder = t.split(".")
        if holder[0] == "www":
            return holder[1]
        else:
            return holder[0]

print(domain_name(url))

### Passed ###

### Answer ###

def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
