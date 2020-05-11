# Input the url and q, q is one word for now

# download HTML of URL
#   grab all html links inside body tag

import urllib3
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
    ## CAVEAT rootHTML needs to be derived from URL
## INPUT (URL, q)
myURL = "http://nrs-projects.humboldt.edu/~st10/s20cs328/328ex-list.php"
#myURL = "http://nrs-projects.humboldt.edu/~st10/f19cs325/325ex-list.php"
#string query
q = "TOO_MANY_ROWS"


rootParC =myURL.count("/")
subHTMLC = myURL.split("/", rootParC) 
rootHTML = ""

for p in range(rootParC):
    rootHTML += subHTMLC[p] + "/"


#print(rootHTML)

uClient = urlopen(myURL)

page_html = uClient.read() #reads all downloaded html page 

uClient.close()
page_soup = soup(page_html, "html.parser") # html parser

rawLinks = []
            #for 328 use 'body', for 325 use 'li'
for a in page_soup.select(' body a[href*=".html"]', href=True):
    #page_soup.select('body 'a[body href*=".html"]) works for 328 but not 325
    #page_soup.select('body a[href*=".html"]', href=True): works for 328
    # XPATH //body/table/tbody/tr/td/span/a
    rawLinks.append(rootHTML + str(a['href']))

print("Number of links found: " + str(len(rawLinks)) + " in given URL. Total links")

# Lets filter out duplicate links
uniqueLinks = rawLinks
rawLinks = list(dict.fromkeys(uniqueLinks))
#print(rawLinks) # print all links as list
print("Number of links found: " + str(len(rawLinks)) + " in given URL. distinct links")
print("crawling links for query...\"" +q +"\"" )

from nltk.text import Text
import nltk, re, pprint
from nltk import word_tokenize
from urllib import request
from urllib.request import urlopen
from urllib import response


### Iterate for the first four appends
fourlinks = []
fourlcontents = []

from re import search

counter = 0
for link in rawLinks:

    if counter <= 3:
        html = urlopen(link).read()
        content = soup(html,features="lxml")
        #remove html element tags
        page = content.get_text()

        #TOKENIZE page
        tokens = word_tokenize(page)

        #filter out duplicate tokens
        distinctTokens = list(dict.fromkeys(tokens))
        textList = Text(distinctTokens)

        # save the link to a list
        #if q in textList or q.find(q) >= 0:
        if q in textList:
            #if counter > 3:
             #   break
            #if search(q, qq ):
            fourlcontents.append(textList)
            fourlinks.append(link)
            counter += 1
    else:
        break

    #here we wanna display the concordances

#print(len(fourlcontents))
print("Links matched for \"" + q +"\": " + str(len(fourlinks)))
        
i = 0

for l in  fourlinks:
    print("\nURL: " + l)
    
    fourlcontents[i].concordance(q)
    i += 1




