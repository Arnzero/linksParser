import nltk
import operator
import urllib3



import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
import re

myURL = "http://nrs-projects.humboldt.edu/~st10/s20cs328/328ex-list.php"

uClient = uReq(myURL)

page_html = uClient.read() #reads all downloaded html page 

uClient.close()
page_soup = soup(page_html, "html.parser") # html parser

all_links = page_soup.find_all("a")
#print(page_soup.select('a[href*=".html"]'))

linksVar = page_soup.select('a[href*=".html"]', href=True)

rawLinks = []
for a in page_soup.select('body a[href*=".html"]', href=True):
    print("Found the URL:", a['href'])
    rawLinks.append(a['href'])

print(len(rawLinks))

#make ABSOLUTE URLs
ABSlinks = []
for a in rawLinks:
    ABSlinks.append("http://nrs-projects.humboldt.edu/~st10/s20cs328/" + str(a))
# hmm maybe we can remove duplicates?
print(ABSlinks[0])
#print(rawLinks[0])



